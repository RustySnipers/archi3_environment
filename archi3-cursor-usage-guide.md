# Archi3 Cursor Usage Guide
## How to Use the Multi-Agent Orchestration System

### Quick Start

Every time you start a project or task in Cursor, the Archi3 system will automatically activate based on the `.cursorrules` file. Here's how to work with it effectively:

## Basic Workflow

### 1. Project Initiation
When starting any project, Cursor will automatically:
- Assess task complexity and domain requirements
- Select appropriate manager and specialist agents
- Create orchestration plan
- Set up project structure

**Example Interaction:**
```
USER: "I need to build a customer dashboard with data analytics"

CURSOR (with Archi3): 
ARCHI3 TASK ANALYSIS:
- Task Type: Development + Analysis (Hybrid)
- Complexity Level: Complex
- Required Agents: @coder-manager (lead) + @analyst-manager (support)
- Estimated Timeline: 4-5 weeks
- Parallel Opportunities: Frontend dev, Backend API, Data analysis, Dashboard design
- Dependencies: Requirements → Architecture → Implementation → Integration → Testing
- Quality Standards: Performance <200ms, Data accuracy >95%, User experience testing

ORCHESTRATION PLAN:
Phase 1: Requirements and Architecture
- @coder-manager: System architecture design
- @analyst-manager: Data requirements and KPI definition
- @backend-developer: API architecture planning
- @frontend-developer: UI/UX design planning
- @bi-analyst: Dashboard metrics specification

[Continues with detailed delegation...]
```

### 2. Understanding Delegation Decisions
Cursor will always explain why certain agents were selected:

**Simple Task Example:**
```
USER: "Fix the login button styling"

CURSOR: This is a Simple task requiring @coder-manager → @frontend-developer
- Single domain (UI development)
- Clear requirements
- Minimal dependencies
- Quick resolution expected
```

**Complex Task Example:**
```
USER: "Launch a new product with full marketing campaign"

CURSOR: This is an Enterprise-level task requiring Full System Orchestration:
- Multiple domains: Development, Analysis, Research, Writing
- Primary: @writer-manager (campaign lead)
- Supporting: @coder-manager (product features), @analyst-manager (metrics), @research-manager (market intelligence)
- Estimated timeline: 6-8 weeks with coordinated phases
```

## Working with Specific Agent Types

### Development Projects
**Trigger Words**: "build", "develop", "code", "implement", "API", "database", "frontend", "backend"

**Example Usage:**
```
USER: "Build a REST API for user management"

CURSOR: Routing to @coder-manager → @backend-developer
- API design and implementation
- Database integration with @database-engineer
- Security implementation
- Testing and documentation
- DevOps deployment preparation with @devops-engineer
```

### Data Analysis Projects
**Trigger Words**: "analyze", "data", "metrics", "insights", "predict", "model", "statistics"

**Example Usage:**
```
USER: "Analyze customer churn patterns and predict future churn"

CURSOR: Routing to @analyst-manager → Multi-specialist coordination
- @statistical-analyst: Churn pattern analysis, hypothesis testing
- @ml-engineer: Predictive model development and validation
- @bi-analyst: Business context and KPI integration
- @visualization-specialist: Dashboard and insight presentation
```

### Research Projects
**Trigger Words**: "research", "find", "investigate", "market analysis", "competitive", "trends"

**Example Usage:**
```
USER: "Research the competitive landscape for AI-powered customer service tools"

CURSOR: Routing to @research-manager → Multi-domain research
- @market-researcher: Industry analysis, market sizing, key players
- @technical-researcher: Feature comparison, technical capabilities
- @news-researcher: Recent developments, funding, partnerships
- Integration and synthesis for comprehensive competitive intelligence
```

### Content Creation Projects
**Trigger Words**: "write", "content", "documentation", "blog", "marketing", "guide", "manual"

**Example Usage:**
```
USER: "Create a comprehensive user onboarding guide with video scripts"

CURSOR: Routing to @writer-manager → Multi-format coordination
- @technical-writer: Step-by-step user guide and documentation
- @creative-writer: Video scripts and engaging narrative elements
- @marketing-copywriter: Onboarding email sequence and CTAs
- Integration for consistent user experience across all materials
```

## Advanced Usage Patterns

### Multi-Domain Projects
For complex projects spanning multiple domains:

```
USER: "Build an AI-powered analytics platform with full documentation and marketing site"

CURSOR: Enterprise-level Multi-Manager Coordination:

PRIMARY COORDINATION:
- @coder-manager: Platform development (lead role)
- @analyst-manager: AI/ML implementation and analytics engine
- @writer-manager: Documentation and marketing content
- @research-manager: AI technology research and competitive analysis

PARALLEL WORKSTREAMS:
Stream 1 (Development): Platform architecture, AI integration, user interface
Stream 2 (Analytics): ML model development, data pipeline, performance metrics
Stream 3 (Content): Technical docs, marketing site, user guides
Stream 4 (Research): Technology validation, market positioning

INTEGRATION POINTS:
- Weekly cross-manager coordination
- Bi-weekly milestone reviews
- Continuous quality assurance
```

### Iterative Development
For ongoing projects with multiple iterations:

```
USER: "Add a new machine learning feature to our existing application"

CURSOR: Moderate Complexity - Multi-manager coordination:
- @coder-manager: Integration architecture, API modifications
- @analyst-manager: ML model development and validation
- Supporting research for feature requirements and user needs
- Documentation updates for new functionality
- Coordinated testing and deployment
```

## Project Structure Management

### Automatic Directory Creation
Cursor automatically creates organized project structures:

```
your-project/
├── archi3/
│   ├── orchestration/
│   │   ├── task-analysis.md
│   │   ├── delegation-plan.md
│   │   └── progress-tracking.md
│   ├── agents/
│   │   ├── manager-reports/
│   │   └── specialist-outputs/
│   └── synthesis/
│       └── final-deliverables/
├── src/ (for development)
├── docs/
├── tests/
└── README.md
```

### File Organization
- All agent outputs are automatically organized and linked
- Version control tracks all changes and decisions
- Integration documents show how components connect
- Progress reports provide transparency into the process

## Quality Assurance Integration

### Automatic Quality Checks
Cursor implements quality gates at every phase:

1. **Requirements Validation**: Ensures all requirements are clear and complete
2. **Agent Selection Validation**: Confirms optimal agent assignment
3. **Progress Monitoring**: Tracks deliverable quality and timeline adherence
4. **Integration Testing**: Validates component compatibility
5. **Final Quality Review**: Comprehensive deliverable assessment

### User Feedback Integration
You can provide feedback at any stage:

```
USER: "The analysis looks good but I need more focus on mobile users"

CURSOR: Updating analysis focus:
- @analyst-manager: Refining analysis to emphasize mobile user behavior
- @bi-analyst: Adding mobile-specific metrics and segmentation
- @visualization-specialist: Creating mobile-focused dashboards
- Updating success criteria to include mobile user insights
```

## Troubleshooting Common Issues

### Agent Selection Concerns
If you disagree with agent selection:

```
USER: "Why did you choose the technical writer instead of the marketing copywriter?"

CURSOR: Agent selection rationale:
- Task focused on user instruction and documentation
- Technical accuracy was prioritized over persuasive messaging
- Target audience identified as existing users needing guidance

Would you like me to adjust the approach?
- Switch to @marketing-copywriter for persuasive messaging
- Use both agents for comprehensive coverage
- Modify the approach based on your specific needs
```

### Timeline or Resource Concerns
For timeline adjustments:

```
USER: "This seems like too long a timeline for what I need"

CURSOR: Adjusting orchestration for faster delivery:
- Identifying tasks that can be simplified or parallelized
- Reducing scope to core requirements
- Switching to single-agent approach where appropriate
- Providing phased delivery options for immediate value

Revised timeline: [Updated estimate]
Quality trade-offs: [What changes with faster timeline]
```

### Quality Concerns
For quality-focused adjustments:

```
USER: "I need higher quality standards for this deliverable"

CURSOR: Implementing enhanced quality assurance:
- Adding peer review cycles
- Including external validation steps
- Implementing additional testing phases
- Increasing documentation requirements
- Adding stakeholder review checkpoints

Impact on timeline: [Additional time required]
Resource implications: [Additional agents or effort needed]
```

## Best Practices for Working with Archi3

### 1. Be Specific About Requirements
```
GOOD: "Build a user authentication system with OAuth2 integration and role-based access control"
BETTER: "Build a secure user authentication system supporting Google OAuth2, with role-based permissions for admin/user/viewer roles, session management, and audit logging"
```

### 2. Clarify Success Criteria
```
GOOD: "Analyze website performance"
BETTER: "Analyze website performance focusing on conversion rates, user engagement metrics, and mobile vs desktop behavior to identify optimization opportunities"
```

### 3. Specify Constraints and Preferences
```
GOOD: "Create marketing content for our new product"
BETTER: "Create B2B marketing content for our new analytics product, targeting technical decision-makers, with focus on ROI and integration capabilities, for LinkedIn and email campaigns"
```

### 4. Provide Context and Background
```
GOOD: "Research market trends"
BETTER: "Research AI-powered customer service market trends to support our Q2 product planning, focusing on enterprise segment growth and competitive positioning"
```

## Monitoring and Optimization

### Progress Tracking
Cursor provides regular status updates:
- Task completion percentages
- Quality metrics and validation results
- Timeline adherence and risk assessments
- Agent performance and utilization

### Performance Optimization
The system continuously learns and improves:
- Agent selection patterns become more accurate
- Timeline estimates improve with experience
- Quality standards adapt to your preferences
- Integration patterns become more efficient

By following this guide, you'll effectively leverage the full power of the Archi3 multi-agent orchestration system through Cursor, ensuring high-quality deliverables, efficient resource utilization, and systematic project management for all your work.
