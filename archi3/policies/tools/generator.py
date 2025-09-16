#!/usr/bin/env python3
"""
Archi3 Policy Generator
Generate policies from templates with variable substitution
"""

import yaml
import json
import os
import sys
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime
import argparse
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Archi3PolicyGenerator:
    """Generate Archi3 policies from templates"""
    
    def __init__(self, policies_dir: str):
        self.policies_dir = Path(policies_dir)
        self.templates_dir = self.policies_dir / "templates"
        self.output_dir = self.policies_dir / "generated"
        
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(exist_ok=True)
    
    def generate_agent_policy(self, template_name: str, variables: Dict[str, str], 
                            output_name: str = None) -> str:
        """Generate an agent policy from template"""
        template_path = self.templates_dir / f"{template_name}.yaml"
        
        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")
        
        # Load template
        with open(template_path, 'r') as f:
            template_content = yaml.safe_load(f)
        
        # Substitute variables
        substituted_content = self._substitute_variables(template_content, variables)
        
        # Generate output filename
        if not output_name:
            output_name = f"{variables.get('AGENT_NAME', 'custom-agent')}-policy"
        
        output_path = self.output_dir / f"{output_name}.yaml"
        
        # Write generated policy
        with open(output_path, 'w') as f:
            yaml.dump(substituted_content, f, default_flow_style=False, sort_keys=False)
        
        logger.info(f"Generated agent policy: {output_path}")
        return str(output_path)
    
    def generate_environment_policy(self, base_environment: str, variables: Dict[str, str],
                                  output_name: str = None) -> str:
        """Generate an environment policy from base environment"""
        base_path = self.policies_dir / "environments" / f"{base_environment}.yaml"
        
        if not base_path.exists():
            raise FileNotFoundError(f"Base environment not found: {base_path}")
        
        # Load base environment
        with open(base_path, 'r') as f:
            base_content = yaml.safe_load(f)
        
        # Apply variable substitutions
        substituted_content = self._substitute_variables(base_content, variables)
        
        # Generate output filename
        if not output_name:
            output_name = f"{variables.get('ENVIRONMENT_NAME', 'custom-env')}"
        
        output_path = self.output_dir / f"{output_name}.yaml"
        
        # Write generated policy
        with open(output_path, 'w') as f:
            yaml.dump(substituted_content, f, default_flow_style=False, sort_keys=False)
        
        logger.info(f"Generated environment policy: {output_path}")
        return str(output_path)
    
    def generate_workflow_policy(self, workflow_type: str, variables: Dict[str, str],
                               output_name: str = None) -> str:
        """Generate a workflow policy"""
        # This would generate orchestration policies for specific workflows
        # For now, we'll create a basic workflow template
        
        workflow_template = {
            "version": "1.0.0",
            "metadata": {
                "name": f"{workflow_type}-workflow",
                "description": f"Workflow policy for {workflow_type}",
                "lastUpdated": datetime.now().isoformat(),
                "author": variables.get("AUTHOR_NAME", "Archi3 System")
            },
            "workflow": {
                "type": workflow_type,
                "phases": variables.get("WORKFLOW_PHASES", []),
                "coordination": {
                    "strategy": variables.get("COORDINATION_STRATEGY", "sequential"),
                    "parallel_execution": variables.get("PARALLEL_EXECUTION", False)
                },
                "quality_gates": variables.get("QUALITY_GATES", []),
                "success_criteria": variables.get("SUCCESS_CRITERIA", [])
            }
        }
        
        # Generate output filename
        if not output_name:
            output_name = f"{workflow_type}-workflow"
        
        output_path = self.output_dir / f"{output_name}.yaml"
        
        # Write generated policy
        with open(output_path, 'w') as f:
            yaml.dump(workflow_template, f, default_flow_style=False, sort_keys=False)
        
        logger.info(f"Generated workflow policy: {output_path}")
        return str(output_path)
    
    def _substitute_variables(self, content: Any, variables: Dict[str, str]) -> Any:
        """Recursively substitute variables in content"""
        if isinstance(content, dict):
            return {key: self._substitute_variables(value, variables) for key, value in content.items()}
        elif isinstance(content, list):
            return [self._substitute_variables(item, variables) for item in content]
        elif isinstance(content, str):
            return self._substitute_string(content, variables)
        else:
            return content
    
    def _substitute_string(self, text: str, variables: Dict[str, str]) -> str:
        """Substitute variables in a string"""
        # Handle {{VARIABLE}} syntax
        pattern = r'\{\{([^}]+)\}\}'
        
        def replace_var(match):
            var_name = match.group(1).strip()
            if var_name in variables:
                return variables[var_name]
            else:
                logger.warning(f"Variable not found: {var_name}")
                return match.group(0)  # Return original if variable not found
        
        return re.sub(pattern, replace_var, text)
    
    def list_templates(self) -> Dict[str, Any]:
        """List available templates"""
        templates = {}
        
        for template_file in self.templates_dir.glob("*.yaml"):
            template_name = template_file.stem
            try:
                with open(template_file, 'r') as f:
                    template_content = yaml.safe_load(f)
                
                # Extract template variables
                variables = self._extract_template_variables(template_content)
                
                templates[template_name] = {
                    "file": str(template_file),
                    "variables": variables,
                    "description": template_content.get("metadata", {}).get("description", "No description")
                }
            except Exception as e:
                logger.warning(f"Failed to load template {template_name}: {e}")
                templates[template_name] = {
                    "file": str(template_file),
                    "error": str(e)
                }
        
        return templates
    
    def _extract_template_variables(self, content: Any) -> List[str]:
        """Extract template variables from content"""
        variables = set()
        
        if isinstance(content, dict):
            for value in content.values():
                variables.update(self._extract_template_variables(value))
        elif isinstance(content, list):
            for item in content:
                variables.update(self._extract_template_variables(item))
        elif isinstance(content, str):
            # Find {{VARIABLE}} patterns
            pattern = r'\{\{([^}]+)\}\}'
            matches = re.findall(pattern, content)
            variables.update(match.strip() for match in matches)
        
        return sorted(list(variables))
    
    def validate_generated_policy(self, policy_path: str) -> Dict[str, Any]:
        """Validate a generated policy"""
        try:
            # Import validator
            sys.path.append(str(self.policies_dir / "tools"))
            from validator import Archi3PolicyValidator
            
            validator = Archi3PolicyValidator(str(self.policies_dir))
            
            # Load and validate the policy
            with open(policy_path, 'r') as f:
                policy_content = yaml.safe_load(f)
            
            # Basic validation
            validation_result = {
                "valid": True,
                "errors": [],
                "warnings": []
            }
            
            # Check required fields
            required_fields = ["version", "metadata", "agents"]
            for field in required_fields:
                if field not in policy_content:
                    validation_result["valid"] = False
                    validation_result["errors"].append(f"Missing required field: {field}")
            
            # Check for unresolved variables
            unresolved_vars = self._find_unresolved_variables(policy_content)
            if unresolved_vars:
                validation_result["warnings"].extend([f"Unresolved variable: {var}" for var in unresolved_vars])
            
            return validation_result
            
        except Exception as e:
            return {
                "valid": False,
                "errors": [str(e)],
                "warnings": []
            }
    
    def _find_unresolved_variables(self, content: Any) -> List[str]:
        """Find unresolved template variables"""
        unresolved = set()
        
        if isinstance(content, dict):
            for value in content.values():
                unresolved.update(self._find_unresolved_variables(value))
        elif isinstance(content, list):
            for item in content:
                unresolved.update(self._find_unresolved_variables(item))
        elif isinstance(content, str):
            # Find {{VARIABLE}} patterns
            pattern = r'\{\{([^}]+)\}\}'
            matches = re.findall(pattern, content)
            unresolved.update(match.strip() for match in matches)
        
        return list(unresolved)

def main():
    """Main CLI interface for policy generation"""
    parser = argparse.ArgumentParser(description="Archi3 Policy Generator")
    parser.add_argument("--policies-dir", default="./archi3/policies",
                       help="Path to policies directory")
    parser.add_argument("--template", required=True,
                       help="Template name to use")
    parser.add_argument("--type", choices=["agent", "environment", "workflow"], 
                       default="agent", help="Type of policy to generate")
    parser.add_argument("--output", help="Output filename")
    parser.add_argument("--variables", help="Variables as JSON string")
    parser.add_argument("--list-templates", action="store_true",
                       help="List available templates")
    parser.add_argument("--validate", action="store_true",
                       help="Validate generated policy")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Verbose output")
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize generator
    generator = Archi3PolicyGenerator(args.policies_dir)
    
    try:
        if args.list_templates:
            templates = generator.list_templates()
            print(json.dumps(templates, indent=2))
            return
        
        # Parse variables
        variables = {}
        if args.variables:
            try:
                variables = json.loads(args.variables)
            except json.JSONDecodeError as e:
                logger.error(f"Invalid JSON for variables: {e}")
                sys.exit(1)
        
        # Generate policy
        if args.type == "agent":
            output_path = generator.generate_agent_policy(args.template, variables, args.output)
        elif args.type == "environment":
            output_path = generator.generate_environment_policy(args.template, variables, args.output)
        elif args.type == "workflow":
            output_path = generator.generate_workflow_policy(args.template, variables, args.output)
        
        print(f"Generated policy: {output_path}")
        
        # Validate if requested
        if args.validate:
            validation_result = generator.validate_generated_policy(output_path)
            if validation_result["valid"]:
                print("✅ Policy validation passed")
            else:
                print("❌ Policy validation failed")
                for error in validation_result["errors"]:
                    print(f"   Error: {error}")
            
            if validation_result["warnings"]:
                print("⚠️  Warnings:")
                for warning in validation_result["warnings"]:
                    print(f"   Warning: {warning}")
            
            if not validation_result["valid"]:
                sys.exit(1)
        
    except Exception as e:
        logger.error(f"Policy generation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
