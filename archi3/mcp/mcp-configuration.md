# Archi3 MCP Configuration Framework
## Model Context Protocol Server Configuration Templates

### 🎯 **Configuration Philosophy**

The MCP configuration system is designed for **maximum flexibility** while maintaining **security and performance**. Each server configuration includes:
- **Activation controls** (enabled/disabled)
- **Permission matrices** (agent-specific access)
- **Security policies** (rate limiting, access controls)
- **Performance settings** (timeouts, resource limits)

### 📁 **Configuration File Structure**

```
archi3/mcp/
├── config/
│   ├── mcp.json                    # Main configuration file
│   ├── servers/                    # Individual server configs
│   │   ├── filesystem.json
│   │   ├── web-browser.json
│   │   ├── database.json
│   │   ├── git.json
│   │   └── api-gateway.json
│   ├── security/                   # Security policies
│   │   ├── permissions.json
│   │   ├── rate-limits.json
│   │   └── audit-config.json
│   └── environments/               # Environment-specific configs
│       ├── development.json
│       ├── staging.json
│       └── production.json
├── templates/                      # Configuration templates
│   ├── server-template.json
│   ├── security-template.json
│   └── environment-template.json
└── scripts/                        # Configuration management
    ├── validate-config.js
    ├── generate-config.js
    └── deploy-config.js
```

### 🔧 **Main Configuration File (mcp.json)**

```json
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
```

### 🗂️ **Individual Server Configurations**

#### File System Server (servers/filesystem.json)
```json
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
```

#### Web Browser Server (servers/web-browser.json)
```json
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
```

#### Database Server (servers/database.json)
```json
{
  "server": {
    "name": "database",
    "description": "Database operations for data analysis and application development",
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-postgres"],
    "env": {
      "NODE_ENV": "production",
      "DATABASE_URL": "${DATABASE_URL}",
      "POOL_SIZE": "5"
    }
  },
  "permissions": {
    "agents": {
      "@analyst-manager": {
        "read": true,
        "write": true,
        "admin": false,
        "schemas": ["public", "analytics"]
      },
      "@database-engineer": {
        "read": true,
        "write": true,
        "admin": true,
        "schemas": ["*"]
      },
      "@bi-analyst": {
        "read": true,
        "write": false,
        "admin": false,
        "schemas": ["public", "analytics", "reports"]
      },
      "@statistical-analyst": {
        "read": true,
        "write": true,
        "admin": false,
        "schemas": ["public", "analytics", "experiments"]
      }
    }
  },
  "security": {
    "connectionString": "${DATABASE_URL}",
    "maxConnections": 5,
    "queryTimeout": "30s",
    "allowedSchemas": ["public", "analytics", "reports", "experiments"],
    "blockedOperations": ["DROP", "TRUNCATE", "ALTER"],
    "auditQueries": true
  },
  "performance": {
    "connectionPoolSize": 5,
    "queryTimeout": "30s",
    "retryAttempts": 3,
    "cacheEnabled": true,
    "cacheTTL": "600s"
  }
}
```

#### Git Server (servers/git.json)
```json
{
  "server": {
    "name": "git",
    "description": "Git repository operations for version control and collaboration",
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-git"],
    "env": {
      "NODE_ENV": "production",
      "GIT_USER_NAME": "${GIT_USER_NAME}",
      "GIT_USER_EMAIL": "${GIT_USER_EMAIL}"
    }
  },
  "permissions": {
    "agents": {
      "@coder-manager": {
        "read": true,
        "write": true,
        "admin": true,
        "repositories": ["*"]
      },
      "@devops-engineer": {
        "read": true,
        "write": true,
        "admin": true,
        "repositories": ["*"]
      },
      "@backend-developer": {
        "read": true,
        "write": true,
        "admin": false,
        "repositories": ["backend", "api", "shared"]
      },
      "@frontend-developer": {
        "read": true,
        "write": true,
        "admin": false,
        "repositories": ["frontend", "ui", "shared"]
      }
    }
  },
  "security": {
    "allowedRepositories": ["*"],
    "blockedOperations": ["force-push", "delete-branch"],
    "requirePullRequest": true,
    "auditCommits": true,
    "maxCommitSize": "10MB"
  },
  "performance": {
    "timeout": "60s",
    "retryAttempts": 2,
    "cacheEnabled": true,
    "cacheTTL": "1800s"
  }
}
```

#### API Gateway Server (servers/api-gateway.json)
```json
{
  "server": {
    "name": "api-gateway",
    "description": "External API integration and management",
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-api-gateway"],
    "env": {
      "NODE_ENV": "production",
      "API_TIMEOUT": "30000",
      "MAX_RETRIES": "3"
    }
  },
  "permissions": {
    "agents": {
      "@research-manager": {
        "apis": ["news", "academic", "market-data"],
        "rateLimit": "100/hour"
      },
      "@analyst-manager": {
        "apis": ["data-sources", "analytics", "visualization"],
        "rateLimit": "200/hour"
      },
      "@writer-manager": {
        "apis": ["content", "translation", "seo"],
        "rateLimit": "50/hour"
      },
      "@coder-manager": {
        "apis": ["github", "package-managers", "deployment"],
        "rateLimit": "500/hour"
      }
    }
  },
  "security": {
    "apiKeys": {
      "github": "${GITHUB_TOKEN}",
      "openai": "${OPENAI_API_KEY}",
      "news": "${NEWS_API_KEY}"
    },
    "rateLimits": {
      "global": "1000/hour",
      "perAgent": "200/hour",
      "perAPI": "100/hour"
    },
    "allowedEndpoints": [
      "api.github.com",
      "api.openai.com",
      "newsapi.org"
    ]
  },
  "performance": {
    "timeout": "30s",
    "retryAttempts": 3,
    "cacheEnabled": true,
    "cacheTTL": "1800s",
    "circuitBreaker": true
  }
}
```

### 🔒 **Security Configuration**

#### Permissions Matrix (security/permissions.json)
```json
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
```

#### Rate Limits (security/rate-limits.json)
```json
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
```

### 🌍 **Environment-Specific Configurations**

#### Development Environment (environments/development.json)
```json
{
  "environment": "development",
  "settings": {
    "debugMode": true,
    "verboseLogging": true,
    "relaxedSecurity": true,
    "mockExternalServices": true
  },
  "servers": {
    "filesystem": {
      "enabled": true,
      "maxFileSize": "50MB",
      "allowedPaths": ["/workspace", "/tmp", "/home"]
    },
    "web-browser": {
      "enabled": true,
      "headless": false,
      "rateLimit": "5 requests/minute"
    },
    "database": {
      "enabled": true,
      "connectionString": "postgresql://localhost:5432/archi3_dev",
      "maxConnections": 2
    }
  }
}
```

#### Production Environment (environments/production.json)
```json
{
  "environment": "production",
  "settings": {
    "debugMode": false,
    "verboseLogging": false,
    "strictSecurity": true,
    "monitoringEnabled": true
  },
  "servers": {
    "filesystem": {
      "enabled": true,
      "maxFileSize": "100MB",
      "allowedPaths": ["/workspace"],
      "auditAllOperations": true
    },
    "web-browser": {
      "enabled": true,
      "headless": true,
      "rateLimit": "10 requests/minute",
      "securityScanning": true
    },
    "database": {
      "enabled": true,
      "connectionString": "${DATABASE_URL}",
      "maxConnections": 5,
      "sslRequired": true
    }
  }
}
```

### 📋 **Configuration Templates**

#### Server Template (templates/server-template.json)
```json
{
  "server": {
    "name": "{{SERVER_NAME}}",
    "description": "{{SERVER_DESCRIPTION}}",
    "command": "{{COMMAND}}",
    "args": {{ARGS_ARRAY}},
    "env": {{ENV_OBJECT}}
  },
  "permissions": {
    "agents": {{AGENT_PERMISSIONS}}
  },
  "security": {
    "{{SECURITY_SETTINGS}}": "{{VALUES}}"
  },
  "performance": {
    "timeout": "{{TIMEOUT}}",
    "retryAttempts": {{RETRY_COUNT}},
    "cacheEnabled": {{CACHE_ENABLED}},
    "cacheTTL": "{{CACHE_TTL}}"
  }
}
```

### 🔧 **Configuration Management Scripts**

#### Configuration Validator (scripts/validate-config.js)
```javascript
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
    this.validateEnvironmentConfigs();
    
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
```

---

*This configuration framework provides a comprehensive, secure, and flexible foundation for MCP server management within the Archi3 ecosystem.*
