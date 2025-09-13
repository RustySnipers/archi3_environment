# Web Application Development Project Template
## Archi3 Orchestration Pattern

### Project Classification
- **Type**: Software Development
- **Complexity**: Complex (Multi-Agent Coordination)
- **Primary Manager**: @coder-manager
- **Secondary Managers**: @analyst-manager (if analytics required), @writer-manager (documentation)
- **Estimated Timeline**: 4-8 weeks
- **Team Size**: 4-6 agents

### Initial Task Analysis Template

```markdown
ARCHI3 TASK ANALYSIS:
- Task Type: Web Application Development
- Complexity Level: Complex
- Required Agents: Full Development Team + Supporting Specialists
- Estimated Timeline: 6 weeks
- Parallel Opportunities: Frontend/Backend development, Database design, DevOps setup
- Dependencies: Requirements → Architecture → Implementation → Testing → Deployment
- Quality Standards: Code coverage >85%, Performance <200ms response time, Security audit passed
```

## Phase-Based Orchestration

### Phase 1: Requirements and Architecture (Week 1)
**Lead Agent**: @coder-manager  
**Coordination**: Multi-agent requirements gathering

```markdown
PHASE 1 DELEGATION PLAN:

Primary Tasks:
├── @coder-manager: Overall architecture design and technology stack selection
├── @backend-developer: API architecture and integration planning
├── @frontend-developer: UI/UX architecture and component planning
├── @database-engineer: Data model design and schema planning
└── @devops-engineer: Infrastructure architecture and deployment strategy

Supporting Tasks (if needed):
├── @research-manager → @technical-researcher: Technology feasibility research
├── @analyst-manager → @bi-analyst: Requirements analysis and metrics definition
└── @writer-manager → @technical-writer: Technical specification documentation

Deliverables:
- System architecture document
- Technology stack selection rationale
- Database schema design
- API specification
- UI/UX wireframes and component hierarchy
- Infrastructure and deployment plan
```

### Phase 2: Core Development (Weeks 2-4)
**Lead Agent**: @coder-manager  
**Coordination**: Parallel development with integration checkpoints

```markdown
PHASE 2 DELEGATION PLAN:

Parallel Development Streams:

Stream 1 - Backend Development:
├── @backend-developer: Core API development, business logic, authentication
├── @database-engineer: Database implementation, optimization, migrations
└── Dependencies: Database schema → API endpoints → Business logic

Stream 2 - Frontend Development:
├── @frontend-developer: UI components, user interactions, responsive design
└── Dependencies: API specification → Component development → Integration

Stream 3 - Infrastructure:
├── @devops-engineer: CI/CD pipeline, development environment, monitoring setup
└── Dependencies: Repository setup → Build automation → Deployment automation

Integration Checkpoints:
- Week 2: Database and basic API endpoints
- Week 3: Frontend components and API integration
- Week 4: End-to-end functionality testing
```

### Phase 3: Integration and Testing (Week 5)
**Lead Agent**: @coder-manager  
**Coordination**: Full team integration and quality assurance

```markdown
PHASE 3 DELEGATION PLAN:

Integration Tasks:
├── @backend-developer: API integration testing, performance optimization
├── @frontend-developer: UI/UX integration, cross-browser testing
├── @database-engineer: Performance optimization, backup procedures
├── @devops-engineer: Production deployment testing, monitoring validation
└── @coder-manager: End-to-end testing coordination, quality gate validation

Quality Assurance:
- Unit test validation (>85% coverage)
- Integration testing across all components
- Performance testing and optimization
- Security testing and vulnerability assessment
- User acceptance testing preparation
```

### Phase 4: Deployment and Documentation (Week 6)
**Lead Agent**: @coder-manager  
**Supporting**: @writer-manager for documentation

```markdown
PHASE 4 DELEGATION PLAN:

Deployment:
├── @devops-engineer: Production deployment, monitoring setup, backup verification
├── @backend-developer: Production database setup, API monitoring
├── @frontend-developer: CDN setup, performance monitoring
└── @database-engineer: Production database optimization, maintenance procedures

Documentation:
├── @writer-manager → @technical-writer: User documentation, API reference
├── @coder-manager: Developer documentation, deployment guides
└── @devops-engineer: Operations and maintenance documentation

Post-Launch:
- Performance monitoring and optimization
- User feedback collection and analysis
- Bug fix prioritization and resolution
- Feature enhancement planning
```

## Communication Templates

### Daily Standup Format
```markdown
DEVELOPMENT TEAM STANDUP - [DATE]

@backend-developer:
- Completed: [Yesterday's work]
- Today: [Today's focus]
- Blockers: [Issues needing resolution]

@frontend-developer:
- Completed: [Yesterday's work]  
- Today: [Today's focus]
- Blockers: [Issues needing resolution]

@database-engineer:
- Completed: [Yesterday's work]
- Today: [Today's focus]
- Blockers: [Issues needing resolution]

@devops-engineer:
- Completed: [Yesterday's work]
- Today: [Today's focus] 
- Blockers: [Issues needing resolution]

Integration Points: [Cross-team dependencies]
Risks: [Project risks and mitigation]
Decisions Needed: [Decisions requiring manager input]
```

### Weekly Progress Report
```json
{
  "project": "web_application_development",
  "week": 3,
  "phase": "core_development",
  "overall_progress": 60,
  "backend_progress": 65,
  "frontend_progress": 58,
  "database_progress": 70,
  "devops_progress": 55,
  "completed_milestones": [
    "Database schema implementation",
    "Core API endpoints",
    "Basic UI components"
  ],
  "current_focus": [
    "API integration testing",
    "Frontend component integration",
    "CI/CD pipeline completion"
  ],
  "blockers": [],
  "risks": [
    "Third-party API integration complexity"
  ],
  "next_week_goals": [
    "Complete frontend-backend integration",
    "Implement authentication flow",
    "Begin end-to-end testing"
  ]
}
```

## Quality Assurance Framework

### Code Quality Standards
```markdown
MANDATORY REQUIREMENTS:
├── Code Coverage: >85% for all components
├── Performance: <200ms API response time, <3s page load
├── Security: OWASP compliance, secure authentication
├── Documentation: Inline comments, README files, API docs
└── Testing: Unit tests, integration tests, E2E tests

CODE REVIEW PROCESS:
1. All code reviewed by peers before merge
2. Automated testing must pass
3. Security scan must pass
4. Performance benchmarks must be met
5. Documentation must be updated
```

### Testing Strategy
```markdown
TESTING HIERARCHY:
├── Unit Tests: Individual function and component testing
├── Integration Tests: API endpoint and database interaction testing
├── Component Tests: Frontend component behavior testing
├── End-to-End Tests: Full user workflow testing
└── Performance Tests: Load testing and optimization validation

TESTING RESPONSIBILITIES:
├── @backend-developer: API unit and integration tests
├── @frontend-developer: Component and UI tests
├── @database-engineer: Database query and migration tests
├── @devops-engineer: Infrastructure and deployment tests
└── @coder-manager: End-to-end and acceptance tests
```

## Risk Management

### Common Risks and Mitigation
```markdown
TECHNICAL RISKS:
├── API Integration Complexity
│   ├── Mitigation: Early prototype development
│   └── Fallback: Alternative API or custom solution
├── Performance Issues
│   ├── Mitigation: Regular performance testing
│   └── Fallback: Architecture optimization or caching layer
├── Security Vulnerabilities
│   ├── Mitigation: Regular security audits
│   └── Fallback: Immediate patching and penetration testing
└── Deployment Issues
    ├── Mitigation: Staging environment testing
    └── Fallback: Rollback procedures and backup systems

PROJECT RISKS:
├── Scope Creep: Clear requirements documentation and change control
├── Resource Constraints: Flexible timeline and priority management
├── Quality Issues: Continuous testing and review processes
└── Integration Delays: Early integration and frequent testing
```

## Success Metrics and KPIs

### Development Metrics
```markdown
VELOCITY METRICS:
├── Story points completed per sprint
├── Code commits and merge frequency
├── Bug fix resolution time
└── Feature completion rate

QUALITY METRICS:
├── Test coverage percentage
├── Bug density (bugs per KLOC)
├── Code review feedback cycles
├── Performance benchmark achievement
└── Security vulnerability count

COLLABORATION METRICS:
├── Cross-team communication frequency
├── Blocker resolution time
├── Knowledge sharing sessions
└── Documentation completeness
```

### User Acceptance Metrics
```markdown
FUNCTIONALITY METRICS:
├── Feature completeness against requirements
├── User workflow success rate
├── Error rate and recovery
└── Performance benchmarks achievement

USER EXPERIENCE METRICS:
├── Page load times and responsiveness
├── UI/UX usability scores
├── Accessibility compliance
└── Cross-browser compatibility
```

## Post-Launch Operations

### Maintenance and Support
```markdown
ONGOING RESPONSIBILITIES:
├── @devops-engineer: Infrastructure monitoring, scaling, security updates
├── @backend-developer: API monitoring, bug fixes, performance optimization
├── @frontend-developer: UI updates, browser compatibility, performance monitoring
└── @database-engineer: Database maintenance, optimization, backup verification

ENHANCEMENT CYCLE:
1. User feedback collection and analysis
2. Feature prioritization and planning
3. Development sprint planning
4. Implementation and testing
5. Deployment and monitoring
```

This template provides a comprehensive orchestration pattern for web application development projects, ensuring systematic coordination, quality delivery, and successful project outcomes through the Archi3 multi-agent system.