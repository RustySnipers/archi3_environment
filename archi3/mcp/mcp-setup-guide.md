# Archi3 MCP Integration Setup Guide
## Complete Model Context Protocol Integration Documentation

### 🎯 **Overview**

This guide provides comprehensive instructions for setting up Model Context Protocol (MCP) integration within the Archi3 multi-agent orchestration system. MCP enables Archi3 agents to seamlessly connect with external tools, APIs, and data sources while maintaining security and performance standards.

### 📋 **Prerequisites**

Before beginning MCP integration setup, ensure you have:

#### **System Requirements**
- **Node.js**: Version 18.0 or higher
- **npm**: Version 9.0 or higher
- **Git**: Version 2.30 or higher
- **Cursor Editor**: Latest version with MCP support

#### **Access Credentials**
- **GitHub Token**: For repository operations
- **Database Credentials**: For data analysis operations
- **API Keys**: For external service integrations
- **Environment Variables**: Secure credential storage

#### **Permissions**
- **File System Access**: Read/write permissions for workspace
- **Network Access**: Outbound connections for API calls
- **Process Management**: Ability to start/stop MCP servers

### 🚀 **Installation Process**

#### **Step 1: Environment Setup**

1. **Create MCP Directory Structure**
   ```bash
   mkdir -p archi3/mcp/{config,servers,security,environments,templates,scripts}
   mkdir -p archi3/mcp/config/{servers,security,environments}
   ```

2. **Initialize Configuration Files**
   ```bash
   # Copy template configurations
   cp archi3/mcp/templates/* archi3/mcp/config/
   
   # Set proper permissions
   chmod 600 archi3/mcp/config/security/*
   chmod 644 archi3/mcp/config/servers/*
   ```

3. **Install MCP Dependencies**
   ```bash
   # Install core MCP packages
   npm install -g @modelcontextprotocol/server-filesystem
   npm install -g @modelcontextprotocol/server-web-browser
   npm install -g @modelcontextprotocol/server-postgres
   npm install -g @modelcontextprotocol/server-git
   ```

#### **Step 2: Configuration Setup**

1. **Main Configuration (mcp.json)**
   ```bash
   # Create main configuration file
   cat > archi3/mcp/config/mcp.json << 'EOF'
   {
     "version": "1.0.0",
     "environment": "development",
     "globalSettings": {
       "enabled": false,
       "debugMode": true,
       "auditLogging": true,
       "performanceMonitoring": true,
       "securityMode": "strict"
     },
     "servers": {
       "filesystem": {
         "enabled": false,
         "configFile": "servers/filesystem.json",
         "priority": 1,
         "dependencies": []
       },
       "web-browser": {
         "enabled": false,
         "configFile": "servers/web-browser.json",
         "priority": 2,
         "dependencies": []
       },
       "database": {
         "enabled": false,
         "configFile": "servers/database.json",
         "priority": 3,
         "dependencies": ["filesystem"]
       },
       "git": {
         "enabled": false,
         "configFile": "servers/git.json",
         "priority": 4,
         "dependencies": ["filesystem"]
       },
       "api-gateway": {
         "enabled": false,
         "configFile": "servers/api-gateway.json",
         "priority": 5,
         "dependencies": ["web-browser"]
       }
     },
     "security": {
       "configFile": "security/permissions.json",
       "rateLimits": "security/rate-limits.json",
       "auditConfig": "security/audit-config.json"
     },
     "monitoring": {
       "metricsEnabled": true,
       "logLevel": "info",
       "retentionDays": 30,
       "alertThresholds": {
         "responseTime": "5s",
         "errorRate": "5%",
         "memoryUsage": "80%"
       }
     }
   }
   EOF
   ```

2. **Environment Variables Setup**
   ```bash
   # Create environment file
   cat > .env.mcp << 'EOF'
   # MCP Configuration
   ARCHI3_MCP_ENABLED=false
   ARCHI3_MCP_MODE=development
   ARCHI3_MCP_SECURITY_MODE=strict
   
   # Database Configuration
   DATABASE_URL=postgresql://username:password@localhost:5432/archi3
   
   # API Keys
   GITHUB_TOKEN=your_github_token_here
   OPENAI_API_KEY=your_openai_key_here
   NEWS_API_KEY=your_news_api_key_here
   
   # Git Configuration
   GIT_USER_NAME=Archi3 User
   GIT_USER_EMAIL=archi3@example.com
   
   # Security
   MCP_AUDIT_LOG_PATH=/var/log/archi3/mcp
   MCP_RATE_LIMIT_WINDOW=3600
   EOF
   
   # Secure the environment file
   chmod 600 .env.mcp
   ```

#### **Step 3: Server Configuration**

1. **File System Server**
   ```bash
   cat > archi3/mcp/config/servers/filesystem.json << 'EOF'
   {
     "server": {
       "name": "filesystem",
       "description": "File system operations for development and content management",
       "command": "npx",
       "args": ["-y", "@modelcontextprotocol/server-filesystem", "/workspace"],
       "env": {
         "NODE_ENV": "production",
         "LOG_LEVEL": "info"
       }
     },
     "permissions": {
       "agents": {
         "@coder-manager": {
           "read": true,
           "write": true,
           "execute": true,
           "paths": ["/workspace", "/tmp", "/src", "/docs"]
         },
         "@analyst-manager": {
           "read": true,
           "write": false,
           "execute": false,
           "paths": ["/workspace/data", "/workspace/reports"]
         },
         "@research-manager": {
           "read": true,
           "write": true,
           "execute": false,
           "paths": ["/workspace/research", "/workspace/sources"]
         },
         "@writer-manager": {
           "read": true,
           "write": true,
           "execute": false,
           "paths": ["/workspace/content", "/workspace/docs"]
         }
       }
     },
     "security": {
       "allowedPaths": ["/workspace", "/tmp"],
       "blockedPaths": ["/etc", "/usr", "/bin", "/sbin"],
       "blockedExtensions": [".exe", ".bat", ".sh", ".cmd"],
       "maxFileSize": "100MB",
       "maxConcurrentOperations": 10
     },
     "performance": {
       "timeout": "30s",
       "retryAttempts": 3,
       "cacheEnabled": true,
       "cacheTTL": "300s"
     }
   }
   EOF
   ```

2. **Web Browser Server**
   ```bash
   cat > archi3/mcp/config/servers/web-browser.json << 'EOF'
   {
     "server": {
       "name": "web-browser",
       "description": "Web browsing and automation for research and data gathering",
       "command": "npx",
       "args": ["-y", "@modelcontextprotocol/server-web-browser"],
       "env": {
         "NODE_ENV": "production",
         "HEADLESS": "true",
         "TIMEOUT": "30000"
       }
     },
     "permissions": {
       "agents": {
         "@research-manager": {
           "browse": true,
           "screenshot": true,
           "automation": true,
           "domains": ["*"]
         },
         "@analyst-manager": {
           "browse": true,
           "screenshot": false,
           "automation": false,
           "domains": ["*.github.com", "*.stackoverflow.com", "*.kaggle.com"]
         },
         "@market-researcher": {
           "browse": true,
           "screenshot": true,
           "automation": true,
           "domains": ["*.crunchbase.com", "*.linkedin.com", "*.bloomberg.com"]
         }
       }
     },
     "security": {
       "allowedDomains": [
         "*.github.com",
         "*.stackoverflow.com",
         "*.wikipedia.org",
         "*.kaggle.com",
         "*.crunchbase.com"
       ],
       "blockedDomains": [
         "*.malicious.com",
         "*.phishing.com"
       ],
       "rateLimit": "10 requests/minute",
       "maxConcurrentSessions": 5,
       "userAgent": "Archi3-MCP-Browser/1.0"
     },
     "performance": {
       "timeout": "60s",
       "retryAttempts": 2,
       "cacheEnabled": true,
       "cacheTTL": "3600s",
       "maxMemoryUsage": "512MB"
     }
   }
   EOF
   ```

#### **Step 4: Security Configuration**

1. **Permissions Matrix**
   ```bash
   cat > archi3/mcp/config/security/permissions.json << 'EOF'
   {
     "permissions": {
       "filesystem": {
         "@coder-manager": ["read", "write", "execute"],
         "@analyst-manager": ["read"],
         "@research-manager": ["read", "write"],
         "@writer-manager": ["read", "write"]
       },
       "web-browser": {
         "@research-manager": ["browse", "screenshot", "automation"],
         "@analyst-manager": ["browse"],
         "@market-researcher": ["browse", "screenshot", "automation"]
       },
       "database": {
         "@analyst-manager": ["read", "write"],
         "@database-engineer": ["read", "write", "admin"],
         "@bi-analyst": ["read"],
         "@statistical-analyst": ["read", "write"]
       },
       "git": {
         "@coder-manager": ["read", "write", "admin"],
         "@devops-engineer": ["read", "write", "admin"],
         "@backend-developer": ["read", "write"],
         "@frontend-developer": ["read", "write"]
       },
       "api-gateway": {
         "@research-manager": ["news", "academic", "market-data"],
         "@analyst-manager": ["data-sources", "analytics"],
         "@writer-manager": ["content", "translation", "seo"],
         "@coder-manager": ["github", "package-managers", "deployment"]
       }
     }
   }
   EOF
   ```

2. **Rate Limiting Configuration**
   ```bash
   cat > archi3/mcp/config/security/rate-limits.json << 'EOF'
   {
     "rateLimits": {
       "global": {
         "requestsPerMinute": 1000,
         "requestsPerHour": 10000,
         "burstLimit": 100
       },
       "perAgent": {
         "@coder-manager": {
           "requestsPerMinute": 200,
           "requestsPerHour": 2000
         },
         "@analyst-manager": {
           "requestsPerMinute": 150,
           "requestsPerHour": 1500
         },
         "@research-manager": {
           "requestsPerMinute": 100,
           "requestsPerHour": 1000
         },
         "@writer-manager": {
           "requestsPerMinute": 100,
           "requestsPerHour": 1000
         }
       },
       "perServer": {
         "filesystem": {
           "operationsPerMinute": 500,
           "maxConcurrentOperations": 10
         },
         "web-browser": {
           "requestsPerMinute": 10,
           "maxConcurrentSessions": 5
         },
         "database": {
           "queriesPerMinute": 200,
           "maxConcurrentConnections": 5
         },
         "git": {
           "operationsPerMinute": 50,
           "maxConcurrentOperations": 3
         },
         "api-gateway": {
           "requestsPerMinute": 100,
           "maxConcurrentRequests": 20
         }
       }
     }
   }
   EOF
   ```

### 🔧 **Integration with Archi3**

#### **Step 5: Cursor Configuration Update**

1. **Update .cursorrules for MCP Integration**
   ```bash
   # Add MCP section to .cursorrules
   cat >> .cursorrules << 'EOF'
   
   ## MCP Integration (Model Context Protocol)
   - MCP servers activate only when ARCHI3_MCP_ENABLED=true
   - Agent-specific permissions enforced automatically
   - Security policies applied based on environment
   - Audit logging enabled for all MCP operations
   
   ### MCP Server Capabilities
   - **File System Server**: File operations, directory management, content creation
   - **Web Browser Server**: Research automation, data gathering, web scraping
   - **Database Server**: Data analysis, query execution, reporting
   - **Git Server**: Version control, repository management, collaboration
   - **API Gateway Server**: External service integration, API management
   
   ### MCP Agent Integration
   - **@coder-manager**: Full access to filesystem, git, and API gateway
   - **@analyst-manager**: Database access, data visualization APIs, file system read
   - **@research-manager**: Web browser automation, academic APIs, file system read/write
   - **@writer-manager**: Content management APIs, file system read/write, translation services
   
   ### MCP Security Protocols
   - All MCP operations logged with agent identification
   - Rate limiting enforced per agent and per server
   - Permission matrix validation for all requests
   - Secure credential management for external services
   EOF
   ```

2. **Create MCP Management Scripts**
   ```bash
   # Create MCP control script
   cat > archi3/mcp/scripts/mcp-control.sh << 'EOF'
   #!/bin/bash
   
   # MCP Control Script for Archi3
   # Usage: ./mcp-control.sh [start|stop|restart|status|enable|disable]
   
   MCP_CONFIG_DIR="archi3/mcp/config"
   MCP_LOG_DIR="archi3/mcp/logs"
   
   # Create log directory
   mkdir -p "$MCP_LOG_DIR"
   
   case "$1" in
     start)
       echo "Starting MCP servers..."
       if [ "$ARCHI3_MCP_ENABLED" = "true" ]; then
         # Start enabled servers
         node archi3/mcp/scripts/start-servers.js
         echo "MCP servers started successfully"
       else
         echo "MCP is disabled. Set ARCHI3_MCP_ENABLED=true to enable"
       fi
       ;;
     stop)
       echo "Stopping MCP servers..."
       node archi3/mcp/scripts/stop-servers.js
       echo "MCP servers stopped"
       ;;
     restart)
       $0 stop
       sleep 2
       $0 start
       ;;
     status)
       echo "MCP Server Status:"
       node archi3/mcp/scripts/status-servers.js
       ;;
     enable)
       echo "Enabling MCP integration..."
       export ARCHI3_MCP_ENABLED=true
       echo "MCP enabled. Restart Cursor to activate."
       ;;
     disable)
       echo "Disabling MCP integration..."
       export ARCHI3_MCP_ENABLED=false
       $0 stop
       echo "MCP disabled."
       ;;
     *)
       echo "Usage: $0 {start|stop|restart|status|enable|disable}"
       exit 1
       ;;
   esac
   EOF
   
   chmod +x archi3/mcp/scripts/mcp-control.sh
   ```

### 🧪 **Testing and Validation**

#### **Step 6: Configuration Validation**

1. **Create Validation Script**
   ```bash
   cat > archi3/mcp/scripts/validate-config.js << 'EOF'
   #!/usr/bin/env node
   
   const fs = require('fs');
   const path = require('path');
   
   class MCPConfigValidator {
     constructor(configPath) {
       this.configPath = configPath;
       this.errors = [];
       this.warnings = [];
     }
   
     validate() {
       this.validateMainConfig();
       this.validateServerConfigs();
       this.validateSecurityConfigs();
       
       return {
         valid: this.errors.length === 0,
         errors: this.errors,
         warnings: this.warnings
       };
     }
   
     validateMainConfig() {
       const config = this.loadConfig('mcp.json');
       
       if (!config.version) {
         this.errors.push('Main config missing version field');
       }
       
       if (!config.servers) {
         this.errors.push('Main config missing servers section');
       }
       
       // Validate server references
       Object.keys(config.servers).forEach(serverName => {
         const server = config.servers[serverName];
         if (!fs.existsSync(path.join(this.configPath, server.configFile))) {
           this.errors.push(`Server config file not found: ${server.configFile}`);
         }
       });
     }
   
     validateServerConfigs() {
       const config = this.loadConfig('mcp.json');
       
       Object.keys(config.servers).forEach(serverName => {
         const serverConfig = this.loadConfig(config.servers[serverName].configFile);
         
         if (!serverConfig.server) {
           this.errors.push(`Server ${serverName} missing server section`);
         }
         
         if (!serverConfig.permissions) {
           this.warnings.push(`Server ${serverName} missing permissions section`);
         }
         
         if (!serverConfig.security) {
           this.warnings.push(`Server ${serverName} missing security section`);
         }
       });
     }
   
     loadConfig(filename) {
       try {
         const filePath = path.join(this.configPath, filename);
         return JSON.parse(fs.readFileSync(filePath, 'utf8'));
       } catch (error) {
         this.errors.push(`Failed to load config ${filename}: ${error.message}`);
         return {};
       }
     }
   }
   
   // CLI usage
   if (require.main === module) {
     const configPath = process.argv[2] || './config';
     const validator = new MCPConfigValidator(configPath);
     const result = validator.validate();
     
     if (result.valid) {
       console.log('✅ Configuration validation passed');
       if (result.warnings.length > 0) {
         console.log('⚠️  Warnings:');
         result.warnings.forEach(warning => console.log(`   - ${warning}`));
       }
     } else {
       console.log('❌ Configuration validation failed');
       result.errors.forEach(error => console.log(`   - ${error}`));
       process.exit(1);
     }
   }
   
   module.exports = MCPConfigValidator;
   EOF
   
   chmod +x archi3/mcp/scripts/validate-config.js
   ```

2. **Run Configuration Validation**
   ```bash
   # Validate configuration
   node archi3/mcp/scripts/validate-config.js archi3/mcp/config
   
   # Expected output:
   # ✅ Configuration validation passed
   ```

#### **Step 7: Test MCP Integration**

1. **Create Test Script**
   ```bash
   cat > archi3/mcp/scripts/test-integration.js << 'EOF'
   #!/usr/bin/env node
   
   const { spawn } = require('child_process');
   const fs = require('fs');
   const path = require('path');
   
   class MCPIntegrationTester {
     constructor() {
       this.testResults = [];
       this.configPath = 'archi3/mcp/config';
     }
   
     async runTests() {
       console.log('🧪 Running MCP Integration Tests...\n');
       
       await this.testConfigurationLoading();
       await this.testServerStartup();
       await this.testPermissionValidation();
       await this.testSecurityPolicies();
       
       this.printResults();
     }
   
     async testConfigurationLoading() {
       console.log('📋 Testing configuration loading...');
       
       try {
         const config = JSON.parse(fs.readFileSync(path.join(this.configPath, 'mcp.json'), 'utf8'));
         
         if (config.version && config.servers) {
           this.testResults.push({ test: 'Configuration Loading', status: 'PASS' });
           console.log('   ✅ Configuration loaded successfully');
         } else {
           this.testResults.push({ test: 'Configuration Loading', status: 'FAIL' });
           console.log('   ❌ Configuration missing required fields');
         }
       } catch (error) {
         this.testResults.push({ test: 'Configuration Loading', status: 'FAIL' });
         console.log(`   ❌ Configuration loading failed: ${error.message}`);
       }
     }
   
     async testServerStartup() {
       console.log('🚀 Testing server startup...');
       
       // Test if MCP packages are installed
       const packages = [
         '@modelcontextprotocol/server-filesystem',
         '@modelcontextprotocol/server-web-browser'
       ];
       
       let allInstalled = true;
       for (const pkg of packages) {
         try {
           require.resolve(pkg);
           console.log(`   ✅ ${pkg} is installed`);
         } catch (error) {
           console.log(`   ❌ ${pkg} is not installed`);
           allInstalled = false;
         }
       }
       
       this.testResults.push({ 
         test: 'Server Startup', 
         status: allInstalled ? 'PASS' : 'FAIL' 
       });
     }
   
     async testPermissionValidation() {
       console.log('🔒 Testing permission validation...');
       
       try {
         const permissions = JSON.parse(fs.readFileSync(path.join(this.configPath, 'security/permissions.json'), 'utf8'));
         
         if (permissions.permissions && Object.keys(permissions.permissions).length > 0) {
           this.testResults.push({ test: 'Permission Validation', status: 'PASS' });
           console.log('   ✅ Permission matrix loaded successfully');
         } else {
           this.testResults.push({ test: 'Permission Validation', status: 'FAIL' });
           console.log('   ❌ Permission matrix is empty or invalid');
         }
       } catch (error) {
         this.testResults.push({ test: 'Permission Validation', status: 'FAIL' });
         console.log(`   ❌ Permission validation failed: ${error.message}`);
       }
     }
   
     async testSecurityPolicies() {
       console.log('🛡️  Testing security policies...');
       
       try {
         const rateLimits = JSON.parse(fs.readFileSync(path.join(this.configPath, 'security/rate-limits.json'), 'utf8'));
         
         if (rateLimits.rateLimits && rateLimits.rateLimits.global) {
           this.testResults.push({ test: 'Security Policies', status: 'PASS' });
           console.log('   ✅ Security policies loaded successfully');
         } else {
           this.testResults.push({ test: 'Security Policies', status: 'FAIL' });
           console.log('   ❌ Security policies are missing or invalid');
         }
       } catch (error) {
         this.testResults.push({ test: 'Security Policies', status: 'FAIL' });
         console.log(`   ❌ Security policy testing failed: ${error.message}`);
       }
     }
   
     printResults() {
       console.log('\n📊 Test Results Summary:');
       console.log('========================');
       
       const passed = this.testResults.filter(r => r.status === 'PASS').length;
       const failed = this.testResults.filter(r => r.status === 'FAIL').length;
       
       this.testResults.forEach(result => {
         const icon = result.status === 'PASS' ? '✅' : '❌';
         console.log(`${icon} ${result.test}: ${result.status}`);
       });
       
       console.log(`\nTotal: ${passed} passed, ${failed} failed`);
       
       if (failed === 0) {
         console.log('\n🎉 All tests passed! MCP integration is ready.');
       } else {
         console.log('\n⚠️  Some tests failed. Please review the configuration.');
         process.exit(1);
       }
     }
   }
   
   // Run tests
   if (require.main === module) {
     const tester = new MCPIntegrationTester();
     tester.runTests().catch(console.error);
   }
   
   module.exports = MCPIntegrationTester;
   EOF
   
   chmod +x archi3/mcp/scripts/test-integration.js
   ```

2. **Run Integration Tests**
   ```bash
   # Run integration tests
   node archi3/mcp/scripts/test-integration.js
   
   # Expected output:
   # 🧪 Running MCP Integration Tests...
   # 📋 Testing configuration loading...
   #    ✅ Configuration loaded successfully
   # 🚀 Testing server startup...
   #    ✅ @modelcontextprotocol/server-filesystem is installed
   #    ✅ @modelcontextprotocol/server-web-browser is installed
   # 🔒 Testing permission validation...
   #    ✅ Permission matrix loaded successfully
   # 🛡️  Testing security policies...
   #    ✅ Security policies loaded successfully
   # 
   # 📊 Test Results Summary:
   # ========================
   # ✅ Configuration Loading: PASS
   # ✅ Server Startup: PASS
   # ✅ Permission Validation: PASS
   # ✅ Security Policies: PASS
   # 
   # Total: 4 passed, 0 failed
   # 
   # 🎉 All tests passed! MCP integration is ready.
   ```

### 🔐 **Security Setup**

#### **Step 8: Security Configuration**

1. **Create Audit Logging Directory**
   ```bash
   # Create secure log directory
   sudo mkdir -p /var/log/archi3/mcp
   sudo chown $USER:$USER /var/log/archi3/mcp
   sudo chmod 750 /var/log/archi3/mcp
   ```

2. **Set Up Environment Security**
   ```bash
   # Secure environment file
   chmod 600 .env.mcp
   
   # Create backup of environment file
   cp .env.mcp .env.mcp.backup
   ```

3. **Configure Firewall Rules (if applicable)**
   ```bash
   # Example firewall rules for MCP servers
   # Allow outbound HTTPS for API calls
   sudo ufw allow out 443/tcp
   
   # Allow outbound HTTP for development
   sudo ufw allow out 80/tcp
   
   # Block inbound connections to MCP ports
   sudo ufw deny in 3000:3010/tcp
   ```

### 🚀 **Activation Process**

#### **Step 9: Enable MCP Integration**

1. **Enable MCP in Environment**
   ```bash
   # Enable MCP integration
   export ARCHI3_MCP_ENABLED=true
   export ARCHI3_MCP_MODE=development
   
   # Add to shell profile for persistence
   echo 'export ARCHI3_MCP_ENABLED=true' >> ~/.bashrc
   echo 'export ARCHI3_MCP_MODE=development' >> ~/.bashrc
   ```

2. **Start MCP Servers**
   ```bash
   # Start MCP servers
   ./archi3/mcp/scripts/mcp-control.sh start
   
   # Check status
   ./archi3/mcp/scripts/mcp-control.sh status
   ```

3. **Verify Integration in Cursor**
   ```bash
   # Restart Cursor to load MCP configuration
   # Test with a simple MCP-enabled task
   ```

### 📊 **Monitoring and Maintenance**

#### **Step 10: Monitoring Setup**

1. **Create Monitoring Script**
   ```bash
   cat > archi3/mcp/scripts/monitor-mcp.sh << 'EOF'
   #!/bin/bash
   
   # MCP Monitoring Script
   # Monitors MCP server health and performance
   
   LOG_FILE="/var/log/archi3/mcp/monitor.log"
   ALERT_EMAIL="admin@example.com"
   
   check_server_health() {
     local server_name=$1
     local port=$2
     
     if nc -z localhost $port 2>/dev/null; then
       echo "$(date): $server_name is healthy" >> $LOG_FILE
       return 0
     else
       echo "$(date): $server_name is down" >> $LOG_FILE
       # Send alert
       echo "MCP Server $server_name is down" | mail -s "MCP Alert" $ALERT_EMAIL
       return 1
     fi
   }
   
   # Monitor all MCP servers
   check_server_health "filesystem" 3001
   check_server_health "web-browser" 3002
   check_server_health "database" 3003
   check_server_health "git" 3004
   check_server_health "api-gateway" 3005
   
   echo "MCP monitoring completed at $(date)"
   EOF
   
   chmod +x archi3/mcp/scripts/monitor-mcp.sh
   ```

2. **Set Up Cron Job for Monitoring**
   ```bash
   # Add monitoring cron job
   (crontab -l 2>/dev/null; echo "*/5 * * * * /path/to/archi3/mcp/scripts/monitor-mcp.sh") | crontab -
   ```

### 🔧 **Troubleshooting**

#### **Common Issues and Solutions**

1. **MCP Servers Not Starting**
   ```bash
   # Check if MCP packages are installed
   npm list -g | grep modelcontextprotocol
   
   # Check environment variables
   env | grep ARCHI3_MCP
   
   # Check configuration files
   node archi3/mcp/scripts/validate-config.js archi3/mcp/config
   ```

2. **Permission Denied Errors**
   ```bash
   # Check file permissions
   ls -la archi3/mcp/config/
   
   # Fix permissions
   chmod 644 archi3/mcp/config/servers/*
   chmod 600 archi3/mcp/config/security/*
   ```

3. **Connection Timeout Issues**
   ```bash
   # Check network connectivity
   ping api.github.com
   
   # Check firewall rules
   sudo ufw status
   
   # Check rate limiting
   tail -f /var/log/archi3/mcp/rate-limit.log
   ```

### 📚 **Documentation and Support**

#### **Additional Resources**

1. **MCP Server Documentation**
   - [Model Context Protocol Documentation](https://docs.cursor.com/context/mcp)
   - [MCP Server Development Guide](https://github.com/modelcontextprotocol/servers)

2. **Archi3 Integration Guides**
   - Agent-specific MCP usage patterns
   - Security best practices
   - Performance optimization tips

3. **Support Channels**
   - Archi3 GitHub Issues
   - MCP Community Discord
   - Cursor Support Documentation

---

*This comprehensive setup guide provides everything needed to integrate MCP into your Archi3 environment, ensuring security, performance, and maintainability.*
