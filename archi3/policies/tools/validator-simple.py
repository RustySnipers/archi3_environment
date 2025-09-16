#!/usr/bin/env python3
"""
Archi3 Policy Validator - Simplified Version
Basic validation framework for Archi3 YAML policies without external dependencies
"""

import yaml
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import argparse
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Archi3PolicyValidator:
    """Simplified policy validation framework for Archi3"""
    
    def __init__(self, policies_dir: str):
        self.policies_dir = Path(policies_dir)
        self.errors = []
        self.warnings = []
        self.validation_results = {}
        
    def validate_all(self) -> Dict[str, Any]:
        """Validate all policies in the policies directory"""
        logger.info("Starting comprehensive policy validation")
        
        # Validate core policies
        core_policies = self._validate_core_policies()
        
        # Validate environment policies
        env_policies = self._validate_environment_policies()
        
        # Validate templates
        template_policies = self._validate_template_policies()
        
        # Cross-policy validation
        cross_validation = self._cross_policy_validation()
        
        # Generate validation report
        report = self._generate_validation_report(
            core_policies, env_policies, template_policies, cross_validation
        )
        
        return report
    
    def validate_specific(self, policy_type: str, policy_name: str = None) -> Dict[str, Any]:
        """Validate specific policy type or policy"""
        logger.info(f"Validating {policy_type}" + (f" - {policy_name}" if policy_name else ""))
        
        if policy_type == "agent-policies":
            return self._validate_core_policies().get("agent-policies", {"valid": False, "error": "Policy not found"})
        elif policy_type == "orchestration-policies":
            return self._validate_core_policies().get("orchestration-policies", {"valid": False, "error": "Policy not found"})
        elif policy_type == "security-policies":
            return self._validate_core_policies().get("security-policies", {"valid": False, "error": "Policy not found"})
        elif policy_type == "environment":
            return self._validate_environment_policies()
        else:
            raise ValueError(f"Unknown policy type: {policy_type}")
    
    def _validate_core_policies(self) -> Dict[str, Any]:
        """Validate core policy files"""
        core_dir = self.policies_dir / "core"
        results = {}
        
        policy_files = [
            "agent-policies.yaml",
            "orchestration-policies.yaml",
            "security-policies.yaml"
        ]
        
        for policy_file in policy_files:
            policy_path = core_dir / policy_file
            if policy_path.exists():
                policy_name = policy_file.replace('.yaml', '')
                results[policy_name] = self._validate_policy_file(policy_path, policy_name)
            else:
                logger.warning(f"Policy file not found: {policy_file}")
                results[policy_file] = {"valid": False, "error": "File not found"}
        
        return results
    
    def _validate_environment_policies(self) -> Dict[str, Any]:
        """Validate environment-specific policy files"""
        env_dir = self.policies_dir / "environments"
        results = {}
        
        if not env_dir.exists():
            logger.warning("Environments directory not found")
            return results
        
        for env_file in env_dir.glob("*.yaml"):
            env_name = env_file.stem
            results[env_name] = self._validate_policy_file(env_file, env_name)
        
        return results
    
    def _validate_template_policies(self) -> Dict[str, Any]:
        """Validate template policy files"""
        template_dir = self.policies_dir / "templates"
        results = {}
        
        if not template_dir.exists():
            logger.warning("Templates directory not found")
            return results
        
        for template_file in template_dir.glob("*.yaml"):
            template_name = template_file.stem
            results[template_name] = self._validate_policy_file(template_file, template_name)
        
        return results
    
    def _validate_policy_file(self, file_path: Path, policy_name: str) -> Dict[str, Any]:
        """Validate a single policy file"""
        try:
            # Load YAML file
            with open(file_path, 'r') as f:
                policy_data = yaml.safe_load(f)
            
            # Basic validation
            validation_result = self._basic_validation(policy_data, policy_name)
            
            # Custom validation rules
            custom_validation = self._apply_custom_validation_rules(policy_data, policy_name)
            
            return {
                "valid": validation_result["valid"] and custom_validation["passed"],
                "file_path": str(file_path),
                "policy_name": policy_name,
                "basic_validation": validation_result,
                "custom_validation": custom_validation,
                "errors": validation_result["errors"] + custom_validation["violations"],
                "warnings": validation_result["warnings"]
            }
            
        except yaml.YAMLError as e:
            return {
                "valid": False,
                "file_path": str(file_path),
                "policy_name": policy_name,
                "error": f"YAML parsing error: {str(e)}",
                "errors": [str(e)],
                "warnings": []
            }
        except Exception as e:
            return {
                "valid": False,
                "file_path": str(file_path),
                "policy_name": policy_name,
                "error": f"Unexpected error: {str(e)}",
                "errors": [str(e)],
                "warnings": []
            }
    
    def _basic_validation(self, policy_data: Dict, policy_name: str) -> Dict[str, Any]:
        """Basic policy validation"""
        errors = []
        warnings = []
        
        # Check required fields
        required_fields = ["version", "metadata"]
        
        for field in required_fields:
            if field not in policy_data:
                errors.append(f"Missing required field: {field}")
        
        # Check version format
        if "version" in policy_data:
            version = policy_data["version"]
            if not isinstance(version, str) or not re.match(r'^\d+\.\d+\.\d+$', version):
                errors.append(f"Invalid version format: {version}")
        
        # Check metadata
        if "metadata" in policy_data:
            metadata = policy_data["metadata"]
            required_metadata = ["name", "description", "lastUpdated", "author"]
            
            for field in required_metadata:
                if field not in metadata:
                    errors.append(f"Missing required metadata field: {field}")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def _apply_custom_validation_rules(self, policy_data: Dict, policy_name: str) -> Dict[str, Any]:
        """Apply custom validation rules specific to Archi3 policies"""
        custom_results = {
            "passed": True,
            "rules_applied": [],
            "violations": []
        }
        
        # Agent ID format validation
        if "agents" in policy_data:
            agent_id_validation = self._validate_agent_ids(policy_data["agents"])
            custom_results["rules_applied"].append("agent-id-format")
            if not agent_id_validation["valid"]:
                custom_results["passed"] = False
                custom_results["violations"].extend(agent_id_validation["violations"])
        
        # Quality standards validation
        if "agents" in policy_data:
            quality_validation = self._validate_quality_standards(policy_data["agents"])
            custom_results["rules_applied"].append("quality-standards")
            if not quality_validation["valid"]:
                custom_results["passed"] = False
                custom_results["violations"].extend(quality_validation["violations"])
        
        # Resource requirements validation
        if "agents" in policy_data:
            resource_validation = self._validate_resource_requirements(policy_data["agents"])
            custom_results["rules_applied"].append("resource-requirements")
            if not resource_validation["valid"]:
                custom_results["passed"] = False
                custom_results["violations"].extend(resource_validation["violations"])
        
        return custom_results
    
    def _validate_agent_ids(self, agents_data: Dict) -> Dict[str, Any]:
        """Validate agent ID format"""
        violations = []
        agent_id_pattern = r'^@[a-z-]+$'
        
        for agent_type, agents in agents_data.items():
            for agent_name, agent_data in agents.items():
                if "id" in agent_data:
                    agent_id = agent_data["id"]
                    if not re.match(agent_id_pattern, agent_id):
                        violations.append(f"Invalid agent ID format: {agent_id} in {agent_name}")
        
        return {
            "valid": len(violations) == 0,
            "violations": violations
        }
    
    def _validate_quality_standards(self, agents_data: Dict) -> Dict[str, Any]:
        """Validate quality standards format"""
        violations = []
        
        for agent_type, agents in agents_data.items():
            for agent_name, agent_data in agents.items():
                if "quality-standards" in agent_data:
                    quality_standards = agent_data["quality-standards"]
                    for metric, value in quality_standards.items():
                        if not self._is_valid_quality_value(value):
                            violations.append(f"Invalid quality value '{value}' for metric '{metric}' in {agent_name}")
        
        return {
            "valid": len(violations) == 0,
            "violations": violations
        }
    
    def _is_valid_quality_value(self, value: str) -> bool:
        """Check if quality value is valid (numeric or percentage)"""
        # Check for percentage format (>90%, <5%, etc.)
        percentage_pattern = r'^[><=]?\d+%$'
        if re.match(percentage_pattern, value):
            return True
        
        # Check for numeric format (<200ms, >1000, etc.)
        numeric_pattern = r'^[><=]?\d+[a-zA-Z]*$'
        if re.match(numeric_pattern, value):
            return True
        
        # Check for boolean format (true, false)
        if value.lower() in ['true', 'false']:
            return True
        
        # Check for text format (required, optional, etc.)
        text_values = ['required', 'optional', 'mandatory', 'recommended', 'none']
        if value.lower() in text_values:
            return True
        
        return False
    
    def _validate_resource_requirements(self, agents_data: Dict) -> Dict[str, Any]:
        """Validate resource requirements format"""
        violations = []
        valid_levels = ['low', 'medium', 'high']
        
        for agent_type, agents in agents_data.items():
            for agent_name, agent_data in agents.items():
                if "resource-requirements" in agent_data:
                    resource_reqs = agent_data["resource-requirements"]
                    for resource, level in resource_reqs.items():
                        if level not in valid_levels:
                            violations.append(f"Invalid resource level '{level}' for {resource} in {agent_name}")
        
        return {
            "valid": len(violations) == 0,
            "violations": violations
        }
    
    def _cross_policy_validation(self) -> Dict[str, Any]:
        """Validate consistency across different policy files"""
        cross_validation = {
            "passed": True,
            "checks_performed": [],
            "violations": []
        }
        
        # Load all policy files for cross-validation
        core_policies = self._load_policy_files(self.policies_dir / "core")
        env_policies = self._load_policy_files(self.policies_dir / "environments")
        
        # Check agent consistency across policies
        agent_consistency = self._check_agent_consistency(core_policies, env_policies)
        cross_validation["checks_performed"].append("agent-consistency")
        if not agent_consistency["valid"]:
            cross_validation["passed"] = False
            cross_validation["violations"].extend(agent_consistency["violations"])
        
        return cross_validation
    
    def _load_policy_files(self, directory: Path) -> Dict[str, Dict]:
        """Load all policy files from a directory"""
        policies = {}
        
        if not directory.exists():
            return policies
        
        for policy_file in directory.glob("*.yaml"):
            try:
                with open(policy_file, 'r') as f:
                    policies[policy_file.stem] = yaml.safe_load(f)
            except Exception as e:
                logger.warning(f"Failed to load {policy_file}: {e}")
        
        return policies
    
    def _check_agent_consistency(self, core_policies: Dict, env_policies: Dict) -> Dict[str, Any]:
        """Check agent consistency across policies"""
        violations = []
        
        # Get agents from core policies
        core_agents = set()
        if "agent-policies" in core_policies and "agents" in core_policies["agent-policies"]:
            agents_data = core_policies["agent-policies"]["agents"]
            for agent_type, agents in agents_data.items():
                for agent_name in agents.keys():
                    core_agents.add(agent_name)
        
        # Check environment policies reference valid agents
        for env_name, env_policy in env_policies.items():
            if "agent-overrides" in env_policy:
                for agent_name in env_policy["agent-overrides"].keys():
                    if agent_name not in core_agents:
                        violations.append(f"Environment {env_name} references unknown agent {agent_name}")
        
        return {
            "valid": len(violations) == 0,
            "violations": violations
        }
    
    def _generate_validation_report(self, core_policies: Dict, env_policies: Dict, 
                                  template_policies: Dict, cross_validation: Dict) -> Dict[str, Any]:
        """Generate comprehensive validation report"""
        total_policies = len(core_policies) + len(env_policies) + len(template_policies)
        valid_policies = sum(1 for policies in [core_policies, env_policies, template_policies] 
                           for policy_result in policies.values() 
                           if policy_result.get("valid", False))
        
        report = {
            "validation_summary": {
                "total_policies": total_policies,
                "valid_policies": valid_policies,
                "invalid_policies": total_policies - valid_policies,
                "validation_timestamp": datetime.now().isoformat(),
                "overall_status": "PASSED" if valid_policies == total_policies and cross_validation["passed"] else "FAILED"
            },
            "core_policies": core_policies,
            "environment_policies": env_policies,
            "template_policies": template_policies,
            "cross_policy_validation": cross_validation,
            "recommendations": self._generate_recommendations(core_policies, env_policies, template_policies, cross_validation)
        }
        
        return report
    
    def _generate_recommendations(self, core_policies: Dict, env_policies: Dict, 
                                template_policies: Dict, cross_validation: Dict) -> List[str]:
        """Generate recommendations based on validation results"""
        recommendations = []
        
        # Check for missing policies
        required_core_policies = ["agent-policies", "orchestration-policies", "security-policies"]
        for policy in required_core_policies:
            if policy not in core_policies:
                recommendations.append(f"Consider creating missing core policy: {policy}")
        
        # Check for environment coverage
        if len(env_policies) < 2:
            recommendations.append("Consider adding more environment-specific policies (staging, testing, etc.)")
        
        # Check for template coverage
        if len(template_policies) < 3:
            recommendations.append("Consider adding more policy templates for common use cases")
        
        # Check for cross-policy issues
        if not cross_validation["passed"]:
            recommendations.append("Address cross-policy validation issues for better consistency")
        
        return recommendations

def main():
    """Main CLI interface for policy validation"""
    parser = argparse.ArgumentParser(description="Archi3 Policy Validator")
    parser.add_argument("--policies-dir", default="./archi3/policies", 
                       help="Path to policies directory")
    parser.add_argument("--type", choices=["all", "agent-policies", "orchestration-policies", 
                                          "security-policies", "environment"], default="all",
                       help="Type of policies to validate")
    parser.add_argument("--name", help="Specific policy name to validate")
    parser.add_argument("--output", help="Output file for validation report")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize validator
    validator = Archi3PolicyValidator(args.policies_dir)
    
    try:
        if args.type == "all":
            results = validator.validate_all()
        else:
            results = validator.validate_specific(args.type, args.name)
        
        # Output results
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"Validation report saved to {args.output}")
        else:
            print(json.dumps(results, indent=2))
        
        # Exit with appropriate code
        if isinstance(results, dict) and "validation_summary" in results:
            if results["validation_summary"]["overall_status"] == "PASSED":
                sys.exit(0)
            else:
                sys.exit(1)
        else:
            sys.exit(0)
            
    except Exception as e:
        logger.error(f"Validation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
