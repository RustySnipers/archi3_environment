# Data Analysis Project Template
## Archi3 Orchestration Pattern

### Project Classification
- **Type**: Data Analytics and Intelligence
- **Complexity**: Moderate to Complex (Multi-Specialist Coordination)
- **Primary Manager**: @analyst-manager
- **Secondary Managers**: @research-manager (data sourcing), @writer-manager (reporting)
- **Estimated Timeline**: 2-4 weeks
- **Team Size**: 3-5 agents

### Initial Task Analysis Template

```markdown
ARCHI3 TASK ANALYSIS:
- Task Type: Data Analysis and Insights
- Complexity Level: Moderate/Complex
- Required Agents: Analysis Team + Supporting Specialists
- Estimated Timeline: 3 weeks
- Parallel Opportunities: Data collection, exploratory analysis, model development
- Dependencies: Data access → Cleaning → Analysis → Validation → Reporting
- Quality Standards: Statistical significance p<0.05, >90% data completeness, peer review validation
```

## Phase-Based Orchestration

### Phase 1: Data Strategy and Collection (Week 1)
**Lead Agent**: @analyst-manager  
**Coordination**: Data sourcing and quality assessment

```markdown
PHASE 1 DELEGATION PLAN:

Primary Tasks:
├── @analyst-manager: Analysis strategy, methodology selection, success metrics definition
├── @bi-analyst: Business context analysis, KPI definition, stakeholder requirements
├── @statistical-analyst: Experimental design, hypothesis formation, power analysis
└── @research-manager → @market-researcher: External data sourcing, benchmark identification

Data Acquisition:
├── @bi-analyst: Internal data source identification and access
├── @statistical-analyst: Sample size calculation and data requirements specification
├── @research-manager: External data validation and integration planning
└── @analyst-manager: Data governance and privacy compliance review

Deliverables:
- Analysis plan and methodology
- Data collection strategy
- Hypothesis framework
- Success criteria and metrics
- Data access and privacy documentation
```

### Phase 2: Data Preparation and Exploration (Week 2)
**Lead Agent**: @analyst-manager  
**Coordination**: Parallel data processing and initial analysis

```markdown
PHASE 2 DELEGATION PLAN:

Data Processing Stream:
├── @bi-analyst: Data cleaning, validation, and integration
├── @statistical-analyst: Data quality assessment, outlier detection
└── @ml-engineer: Feature engineering, data transformation (if ML required)

Exploratory Analysis Stream:
├── @bi-analyst: Descriptive statistics, business metric calculation
├── @statistical-analyst: Correlation analysis, distribution testing
├── @visualization-specialist: Initial data visualization, pattern identification
└── @ml-engineer: Preliminary modeling assessment (if predictive analysis required)

Quality Assurance:
- Data completeness and accuracy validation
- Statistical assumption testing
- Business logic verification
- Documentation of data transformations

Integration Checkpoints:
- Mid-week: Data quality assessment
- End-week: Exploratory analysis summary
```

### Phase 3: Advanced Analysis and Modeling (Week 3)
**Lead Agent**: @analyst-manager  
**Coordination**: Specialized analysis execution

```markdown
PHASE 3 DELEGATION PLAN:

Analysis Execution:
├── @statistical-analyst: Hypothesis testing, confidence intervals, significance testing
├── @ml-engineer: Predictive modeling, algorithm selection, validation (if required)
├── @bi-analyst: Business intelligence analysis, trend identification
└── @visualization-specialist: Advanced visualizations, interactive dashboards

Validation and Review:
├── @statistical-analyst: Peer review of statistical methodology and results
├── @ml-engineer: Model validation, cross-validation, performance assessment
├── @analyst-manager: Results integration, business interpretation
└── Cross-validation with @research-manager for external data consistency

Key Activities:
- Statistical significance testing
- Model development and validation
- Business impact assessment
- Insight development and validation
```

### Phase 4: Reporting and Presentation (Week 4)
**Lead Agent**: @analyst-manager  
**Supporting**: @writer-manager for professional reporting

```markdown
PHASE 4 DELEGATION PLAN:

Report Development:
├── @analyst-manager: Executive summary, key findings synthesis
├── @writer-manager → @academic-writer: Formal methodology documentation
├── @writer-manager → @technical-writer: Technical appendix and documentation
└── @visualization-specialist: Final visualizations, presentation graphics

Stakeholder Communication:
├── @bi-analyst: Business impact summary, recommendation development
├── @statistical-analyst: Statistical methodology and confidence documentation
├── @visualization-specialist: Dashboard creation, interactive presentations
└── @analyst-manager: Stakeholder presentation and Q&A preparation

Quality Assurance:
- Peer review of all findings and methodology
- Statistical rigor validation
- Business relevance confirmation
- Presentation clarity and accuracy review
```

## Analysis Type Specializations

### Business Intelligence Analysis
**Team**: @bi-analyst (lead) + @statistical-analyst + @visualization-specialist
```markdown
FOCUS AREAS:
├── KPI tracking and trend analysis
├── Performance dashboard development  
├── Business metric correlation analysis
├── Revenue and cost impact assessment
└── Operational efficiency measurement

DELIVERABLES:
- Executive KPI dashboard
- Business performance report
- Trend analysis and forecasting
- Operational recommendations
```

### Predictive Modeling Project
**Team**: @ml-engineer (lead) + @statistical-analyst + @bi-analyst + @visualization-specialist
```markdown
FOCUS AREAS:
├── Feature engineering and selection
├── Algorithm development and tuning
├── Model validation and testing
├── Performance monitoring setup
└── Business impact prediction

DELIVERABLES:
- Trained predictive model
- Model performance documentation
- Deployment recommendations
- Monitoring and maintenance plan
```

### Statistical Research Study
**Team**: @statistical-analyst (lead) + @bi-analyst + @visualization-specialist
```markdown
FOCUS AREAS:
├── Experimental design and hypothesis testing
├── Statistical significance assessment
├── Confidence interval calculation
├── Effect size determination
└── Research methodology validation

DELIVERABLES:
- Statistical analysis report
- Hypothesis test results
- Research methodology documentation
- Statistical significance assessment
```

### Market Analysis Project
**Team**: @bi-analyst (lead) + @statistical-analyst + @research-manager → @market-researcher
```markdown
FOCUS AREAS:
├── Market size and growth analysis
├── Competitive positioning assessment
├── Customer segmentation analysis
├── Market opportunity identification
└── Strategic recommendation development

DELIVERABLES:
- Market analysis report
- Competitive landscape assessment
- Customer segmentation insights
- Strategic recommendations
```

## Quality Assurance Framework

### Statistical Rigor Standards
```markdown
METHODOLOGY REQUIREMENTS:
├── Hypothesis clearly defined before analysis
├── Appropriate statistical tests for data type and distribution
├── Multiple comparison corrections applied when necessary
├── Confidence intervals reported with point estimates
├── Effect sizes calculated and interpreted
├── Assumptions tested and validated
└── Limitations and caveats clearly documented

REPRODUCIBILITY STANDARDS:
├── All analysis code documented and version controlled
├── Data sources and transformations documented
├── Random seeds set for reproducible results
├── Analysis workflow clearly documented
└── Peer review of methodology and results
```

### Data Quality Standards
```markdown
DATA VALIDATION REQUIREMENTS:
├── Completeness: >90% for key variables
├── Accuracy: Cross-validation with source systems
├── Consistency: Logic checks and business rule validation
├── Currency: Data freshness appropriate for analysis
├── Relevance: Direct connection to analysis objectives
└── Privacy: Compliance with data governance policies

DOCUMENTATION REQUIREMENTS:
├── Data dictionary with variable definitions
├── Data lineage and transformation documentation
├── Quality assessment reports
├── Privacy and ethics compliance documentation
└── Data retention and disposal procedures
```

## Communication Templates

### Analysis Status Update
```json
{
  "analysis_project_id": "analysis_001",
  "phase": "advanced_analysis",
  "progress": 75,
  "team_active": ["statistical-analyst", "ml-engineer", "visualization-specialist"],
  "data_quality": {
    "completeness": 94,
    "accuracy": 98,
    "validation_status": "passed"
  },
  "key_findings": [
    "Significant correlation between X and Y (r=0.67, p<0.001)",
    "Customer segment A shows 23% higher conversion rate",
    "Seasonal pattern identified with 89% confidence"
  ],
  "current_tasks": [
    "Predictive model validation",
    "Interactive dashboard development",
    "Statistical significance testing"
  ],
  "next_milestones": [
    "Model deployment recommendation",
    "Executive presentation preparation"
  ],
  "estimated_completion": "2024-02-01T17:00:00Z"
}
```

### Agent Delegation Format for Analysis
```markdown
ANALYSIS DELEGATION:
To: @[analyst-agent]
Project: [Analysis Project Name]
Analysis Type: [Descriptive/Inferential/Predictive/Prescriptive]
Data Sources: [Available datasets and access methods]
Business Question: [Specific question to be answered]
Methodology: [Required or preferred analytical approach]
Success Criteria: [Statistical and business success measures]
Timeline: [Analysis completion deadline]
Quality Standards: [Statistical rigor and validation requirements]
Deliverables: [Expected outputs and formats]
Stakeholder Context: [Who will use results and how]
```

## Risk Management

### Analysis Risks and Mitigation
```markdown
DATA RISKS:
├── Incomplete or Missing Data
│   ├── Mitigation: Multiple data sources, imputation strategies
│   └── Fallback: Reduced scope analysis, sensitivity testing
├── Data Quality Issues
│   ├── Mitigation: Comprehensive data validation processes
│   └── Fallback: Quality adjustment modeling, limitation documentation
├── Privacy/Compliance Violations
│   ├── Mitigation: Early privacy review, anonymization procedures
│   └── Fallback: Alternative data sources, aggregated analysis
└── External Data Changes
    ├── Mitigation: Multiple data sources, real-time monitoring
    └── Fallback: Historical analysis, alternative benchmarks

ANALYTICAL RISKS:
├── Statistical Significance Issues
│   ├── Mitigation: Power analysis, sample size calculation
│   └── Fallback: Effect size reporting, confidence intervals
├── Model Overfitting
│   ├── Mitigation: Cross-validation, holdout testing
│   └── Fallback: Simplified models, ensemble methods
├── Business Relevance Gap
│   ├── Mitigation: Stakeholder involvement, business context review
│   └── Fallback: Alternative analysis approaches, additional validation
└── Reproducibility Issues
    ├── Mitigation: Code documentation, version control
    └── Fallback: Alternative analysis methods, peer review
```

## Success Metrics and Validation

### Analysis Quality Metrics
```markdown
TECHNICAL METRICS:
├── Statistical power and effect sizes
├── Model performance metrics (accuracy, precision, recall)
├── Cross-validation results and stability
├── Data quality scores (completeness, accuracy)
└── Reproducibility verification

BUSINESS IMPACT METRICS:
├── Decision support quality and actionability
├── Stakeholder satisfaction with insights
├── Business outcome prediction accuracy
├── Cost-benefit analysis of recommendations
└── Long-term validation of predictions
```

### Stakeholder Satisfaction
```markdown
DELIVERY METRICS:
├── Timeliness of analysis completion
├── Clarity and accessibility of results
├── Actionability of recommendations
├── Statistical rigor and confidence
└── Visualization effectiveness and impact
```

## Post-Analysis Operations

### Follow-up and Monitoring
```markdown
ONGOING RESPONSIBILITIES:
├── @ml-engineer: Model performance monitoring, retraining schedules
├── @bi-analyst: Business metric tracking, outcome validation
├── @statistical-analyst: Methodology refinement, assumption validation
└── @visualization-specialist: Dashboard maintenance, user feedback integration

CONTINUOUS IMPROVEMENT:
1. Result validation against actual outcomes
2. Methodology refinement based on learnings
3. Model performance monitoring and updates
4. Stakeholder feedback integration
5. Knowledge transfer and documentation updates
```

This template provides comprehensive orchestration for data analysis projects, ensuring statistical rigor, business relevance, and actionable insights through coordinated specialist expertise.