#!/usr/bin/env python3
"""
Archi3 Policy Deployer
Deploy policies to different environments with validation and rollback
"""

import yaml
import json
import os
import sys
import shutil
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime
import argparse
import logging
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Archi3PolicyDeployer:
    """Deploy Archi3 policies to different environments"""
    
    def __init__(self, policies_dir: str):
        self.policies_dir = Path(policies_dir)
        self.core_dir = self.policies_dir / "core"
        self.environments_dir = self.policies_dir / "environments"
        self.deployments_dir = self.policies_dir / "deployments"
        self.backup_dir = self.policies_dir / "backups"
        
        # Create necessary directories
        self.deployments_dir.mkdir(exist_ok=True)
        self.backup_dir.mkdir(exist_ok=True)
    
    def deploy_to_environment(self, environment: str, validate: bool = True, 
                            backup: bool = True, dry_run: bool = False) -> Dict[str, Any]:
        """Deploy policies to a specific environment"""
        logger.info(f"Deploying policies to environment: {environment}")
        
        deployment_result = {
            "environment": environment,
            "timestamp": datetime.now().isoformat(),
            "success": False,
            "steps": [],
            "errors": [],
            "warnings": []
        }
        
        try:
            # Step 1: Validate policies
            if validate:
                validation_result = self._validate_policies()
                deployment_result["steps"].append("validation")
                if not validation_result["valid"]:
                    deployment_result["errors"].extend(validation_result["errors"])
                    return deployment_result
            
            # Step 2: Create backup
            if backup and not dry_run:
                backup_result = self._create_backup(environment)
                deployment_result["steps"].append("backup")
                if not backup_result["success"]:
                    deployment_result["warnings"].append("Backup creation failed")
            
            # Step 3: Deploy core policies
            if not dry_run:
                core_deployment = self._deploy_core_policies()
                deployment_result["steps"].append("core-deployment")
                if not core_deployment["success"]:
                    deployment_result["errors"].extend(core_deployment["errors"])
                    return deployment_result
            
            # Step 4: Deploy environment-specific policies
            if not dry_run:
                env_deployment = self._deploy_environment_policies(environment)
                deployment_result["steps"].append("environment-deployment")
                if not env_deployment["success"]:
                    deployment_result["errors"].extend(env_deployment["errors"])
                    return deployment_result
            
            # Step 5: Apply policy overrides
            if not dry_run:
                override_result = self._apply_policy_overrides(environment)
                deployment_result["steps"].append("policy-overrides")
                if not override_result["success"]:
                    deployment_result["warnings"].append("Some policy overrides failed")
            
            # Step 6: Verify deployment
            verification_result = self._verify_deployment(environment)
            deployment_result["steps"].append("verification")
            if not verification_result["success"]:
                deployment_result["warnings"].extend(verification_result["warnings"])
            
            # Step 7: Update deployment history
            if not dry_run:
                self._update_deployment_history(deployment_result)
            
            deployment_result["success"] = True
            logger.info(f"Successfully deployed to {environment}")
            
        except Exception as e:
            logger.error(f"Deployment failed: {e}")
            deployment_result["errors"].append(str(e))
        
        return deployment_result
    
    def rollback_deployment(self, environment: str, deployment_id: str = None) -> Dict[str, Any]:
        """Rollback deployment to previous version"""
        logger.info(f"Rolling back deployment for environment: {environment}")
        
        rollback_result = {
            "environment": environment,
            "timestamp": datetime.now().isoformat(),
            "success": False,
            "steps": [],
            "errors": []
        }
        
        try:
            # Find backup to restore
            backup_path = self._find_backup(environment, deployment_id)
            if not backup_path:
                rollback_result["errors"].append("No backup found for rollback")
                return rollback_result
            
            # Restore from backup
            restore_result = self._restore_from_backup(backup_path)
            rollback_result["steps"].append("restore")
            if not restore_result["success"]:
                rollback_result["errors"].extend(restore_result["errors"])
                return rollback_result
            
            # Verify rollback
            verification_result = self._verify_deployment(environment)
            rollback_result["steps"].append("verification")
            if not verification_result["success"]:
                rollback_result["errors"].extend(verification_result["errors"])
                return rollback_result
            
            rollback_result["success"] = True
            logger.info(f"Successfully rolled back {environment}")
            
        except Exception as e:
            logger.error(f"Rollback failed: {e}")
            rollback_result["errors"].append(str(e))
        
        return rollback_result
    
    def list_deployments(self, environment: str = None) -> List[Dict[str, Any]]:
        """List deployment history"""
        deployments = []
        
        history_file = self.deployments_dir / "deployment-history.json"
        if history_file.exists():
            with open(history_file, 'r') as f:
                all_deployments = json.load(f)
            
            if environment:
                deployments = [d for d in all_deployments if d.get("environment") == environment]
            else:
                deployments = all_deployments
        
        return deployments
    
    def _validate_policies(self) -> Dict[str, Any]:
        """Validate all policies before deployment"""
        try:
            # Import validator
            sys.path.append(str(self.policies_dir / "tools"))
            from validator import Archi3PolicyValidator
            
            validator = Archi3PolicyValidator(str(self.policies_dir))
            validation_result = validator.validate_all()
            
            return {
                "valid": validation_result["validation_summary"]["overall_status"] == "PASSED",
                "errors": [] if validation_result["validation_summary"]["overall_status"] == "PASSED" else ["Policy validation failed"],
                "details": validation_result
            }
            
        except Exception as e:
            return {
                "valid": False,
                "errors": [str(e)]
            }
    
    def _create_backup(self, environment: str) -> Dict[str, Any]:
        """Create backup of current deployment"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{environment}_{timestamp}"
            backup_path = self.backup_dir / backup_name
            
            # Create backup directory
            backup_path.mkdir(exist_ok=True)
            
            # Copy core policies
            if self.core_dir.exists():
                shutil.copytree(self.core_dir, backup_path / "core")
            
            # Copy environment policies
            if self.environments_dir.exists():
                shutil.copytree(self.environments_dir, backup_path / "environments")
            
            # Create backup metadata
            backup_metadata = {
                "environment": environment,
                "timestamp": datetime.now().isoformat(),
                "backup_path": str(backup_path),
                "files": list(backup_path.rglob("*"))
            }
            
            with open(backup_path / "backup-metadata.json", 'w') as f:
                json.dump(backup_metadata, f, indent=2)
            
            return {
                "success": True,
                "backup_path": str(backup_path),
                "backup_name": backup_name
            }
            
        except Exception as e:
            return {
                "success": False,
                "errors": [str(e)]
            }
    
    def _deploy_core_policies(self) -> Dict[str, Any]:
        """Deploy core policies"""
        try:
            # Core policies are already in place, just verify they exist
            required_core_policies = [
                "agent-policies.yaml",
                "orchestration-policies.yaml",
                "security-policies.yaml"
            ]
            
            missing_policies = []
            for policy_file in required_core_policies:
                if not (self.core_dir / policy_file).exists():
                    missing_policies.append(policy_file)
            
            if missing_policies:
                return {
                    "success": False,
                    "errors": [f"Missing core policies: {missing_policies}"]
                }
            
            return {"success": True}
            
        except Exception as e:
            return {
                "success": False,
                "errors": [str(e)]
            }
    
    def _deploy_environment_policies(self, environment: str) -> Dict[str, Any]:
        """Deploy environment-specific policies"""
        try:
            env_policy_file = self.environments_dir / f"{environment}.yaml"
            
            if not env_policy_file.exists():
                return {
                    "success": False,
                    "errors": [f"Environment policy not found: {env_policy_file}"]
                }
            
            # Environment policies are already in place
            # In a real deployment, you would copy them to the target system
            return {"success": True}
            
        except Exception as e:
            return {
                "success": False,
                "errors": [str(e)]
            }
    
    def _apply_policy_overrides(self, environment: str) -> Dict[str, Any]:
        """Apply environment-specific policy overrides"""
        try:
            # Load environment policy
            env_policy_file = self.environments_dir / f"{environment}.yaml"
            with open(env_policy_file, 'r') as f:
                env_policy = yaml.safe_load(f)
            
            # Apply overrides (in a real system, this would modify the running configuration)
            overrides_applied = []
            
            if "agent-overrides" in env_policy:
                overrides_applied.append("agent-overrides")
            
            if "mcp-servers" in env_policy:
                overrides_applied.append("mcp-servers")
            
            if "security-overrides" in env_policy:
                overrides_applied.append("security-overrides")
            
            return {
                "success": True,
                "overrides_applied": overrides_applied
            }
            
        except Exception as e:
            return {
                "success": False,
                "errors": [str(e)]
            }
    
    def _verify_deployment(self, environment: str) -> Dict[str, Any]:
        """Verify deployment was successful"""
        try:
            verification_result = {
                "success": True,
                "warnings": []
            }
            
            # Check if core policies are accessible
            core_policies = list(self.core_dir.glob("*.yaml"))
            if len(core_policies) < 3:
                verification_result["warnings"].append("Some core policies may be missing")
            
            # Check if environment policy exists
            env_policy = self.environments_dir / f"{environment}.yaml"
            if not env_policy.exists():
                verification_result["success"] = False
                verification_result["warnings"].append(f"Environment policy not found: {env_policy}")
            
            return verification_result
            
        except Exception as e:
            return {
                "success": False,
                "warnings": [str(e)]
            }
    
    def _update_deployment_history(self, deployment_result: Dict[str, Any]):
        """Update deployment history"""
        history_file = self.deployments_dir / "deployment-history.json"
        
        # Load existing history
        history = []
        if history_file.exists():
            with open(history_file, 'r') as f:
                history = json.load(f)
        
        # Add new deployment
        history.append(deployment_result)
        
        # Keep only last 100 deployments
        if len(history) > 100:
            history = history[-100:]
        
        # Save updated history
        with open(history_file, 'w') as f:
            json.dump(history, f, indent=2)
    
    def _find_backup(self, environment: str, deployment_id: str = None) -> Optional[Path]:
        """Find backup for rollback"""
        if deployment_id:
            # Find specific backup
            backup_path = self.backup_dir / deployment_id
            if backup_path.exists():
                return backup_path
        else:
            # Find latest backup for environment
            env_backups = list(self.backup_dir.glob(f"{environment}_*"))
            if env_backups:
                # Sort by timestamp and return latest
                env_backups.sort(key=lambda x: x.name)
                return env_backups[-1]
        
        return None
    
    def _restore_from_backup(self, backup_path: Path) -> Dict[str, Any]:
        """Restore from backup"""
        try:
            # Load backup metadata
            metadata_file = backup_path / "backup-metadata.json"
            if metadata_file.exists():
                with open(metadata_file, 'r') as f:
                    metadata = json.load(f)
            
            # Restore core policies
            core_backup = backup_path / "core"
            if core_backup.exists():
                if self.core_dir.exists():
                    shutil.rmtree(self.core_dir)
                shutil.copytree(core_backup, self.core_dir)
            
            # Restore environment policies
            env_backup = backup_path / "environments"
            if env_backup.exists():
                if self.environments_dir.exists():
                    shutil.rmtree(self.environments_dir)
                shutil.copytree(env_backup, self.environments_dir)
            
            return {"success": True}
            
        except Exception as e:
            return {
                "success": False,
                "errors": [str(e)]
            }

def main():
    """Main CLI interface for policy deployment"""
    parser = argparse.ArgumentParser(description="Archi3 Policy Deployer")
    parser.add_argument("--policies-dir", default="./archi3/policies",
                       help="Path to policies directory")
    parser.add_argument("--environment", required=True,
                       help="Target environment")
    parser.add_argument("--action", choices=["deploy", "rollback", "list"], 
                       default="deploy", help="Action to perform")
    parser.add_argument("--deployment-id", help="Deployment ID for rollback")
    parser.add_argument("--validate", action="store_true", default=True,
                       help="Validate policies before deployment")
    parser.add_argument("--no-backup", action="store_true",
                       help="Skip backup creation")
    parser.add_argument("--dry-run", action="store_true",
                       help="Perform dry run without actual deployment")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Verbose output")
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize deployer
    deployer = Archi3PolicyDeployer(args.policies_dir)
    
    try:
        if args.action == "deploy":
            result = deployer.deploy_to_environment(
                args.environment,
                validate=args.validate,
                backup=not args.no_backup,
                dry_run=args.dry_run
            )
            
            if result["success"]:
                print(f"✅ Successfully deployed to {args.environment}")
                print(f"Steps completed: {', '.join(result['steps'])}")
            else:
                print(f"❌ Deployment to {args.environment} failed")
                for error in result["errors"]:
                    print(f"   Error: {error}")
                sys.exit(1)
            
            if result["warnings"]:
                print("⚠️  Warnings:")
                for warning in result["warnings"]:
                    print(f"   Warning: {warning}")
        
        elif args.action == "rollback":
            result = deployer.rollback_deployment(args.environment, args.deployment_id)
            
            if result["success"]:
                print(f"✅ Successfully rolled back {args.environment}")
                print(f"Steps completed: {', '.join(result['steps'])}")
            else:
                print(f"❌ Rollback of {args.environment} failed")
                for error in result["errors"]:
                    print(f"   Error: {error}")
                sys.exit(1)
        
        elif args.action == "list":
            deployments = deployer.list_deployments(args.environment)
            
            if deployments:
                print(f"Deployment history for {args.environment}:")
                for deployment in deployments[-10:]:  # Show last 10
                    status = "✅" if deployment["success"] else "❌"
                    timestamp = deployment["timestamp"]
                    print(f"   {status} {timestamp}")
            else:
                print(f"No deployments found for {args.environment}")
        
    except Exception as e:
        logger.error(f"Deployment operation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
