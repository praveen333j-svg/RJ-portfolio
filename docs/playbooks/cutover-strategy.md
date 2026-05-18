# The Cutover Playbook: Embracing the Delta

> *"Don't hope D-Day will be Blue Skies... Be paranoid in the lead-up in a good way. That's how you earn a good night's sleep and wake up confident and full of energy on D-Day."*

Production Reality: Testing will never fully replicate production. That is not a failure of capability; it is a structural reality. 

No matter how mature the test environment, how comprehensive the coverage, or how seasoned the QA team, testing cannot fully eliminate risk due to environmental divergence and constraints. The real exposure often sits below the application layer. System-level settings, such as COBOL compiler options or runtime parameters, have poor visibility. Certain scenarios only become visible for the first time after go-live in the production environment.

Effective risk management begins by acknowledging the delta rather than attempting to eliminate it. The objective is to identify where failure is plausible, and design containment before impact becomes material.

---
<div style="text-align: center; margin: 30px 0;">
  <img src="/assets/4-ps-u.png" alt="Leadership Operating Principles" style="max-width: 100%; border: 1px solid #ffbf00; border-radius: 4px; box-shadow: 0 4px 8px rgba(0,0,0,0.5);">
  <p style="font-size: 0.85em; color: #ccc; margin-top: 10px;"><em>Figure 1: Leadership Operating Principles</em></p>
</div>
## The Two Critical Risk Parameters

Risk is not defined solely by the probability of failure. It is shaped by how quickly failure spreads, how broadly it propagates, and how visible it becomes.

* **Impact Latency Window (ILW):** The time between when a defect occurs and when a customer or regulator becomes aware of it.
* **Impact Amplification Window (IAW):** The point at which an isolated defect begins to compound into widespread operational, financial, or reputational damage.

---

## The Five Principles of Cutover

I have built my cutover playbook based on five principles:

### 1. Focus on the Grey Areas
Start with what cannot be evaluated faithfully in QA. Where production conditions diverge, documentation becomes less dependable, and experience becomes critical. These are the zones where surprises emerge. Test coverage metrics alone are not a proxy for safety.

### 2. Prioritise Risk with Objective Scoring
Intuition has limits, especially under deadline pressure. A structured framework such as Failure Mode and Effects Analysis (FMEA) imposes discipline: assess severity, likelihood, and detectability, then rank exposures accordingly. Prioritisation is a strategy.

### 3. Reduce Customer Exposure
Containment begins with volume control. Consider posting the transaction after the major go-live event. The critical question is simple: must every transaction file be processed immediately, or can exposure be deliberately constrained? Reducing exposure converts potential crises into manageable operational issues.

### 4. Maximise the Impact Latency Window
Timing decisions are often treated as logistical details. They are strategic controls. If a cutover occurs just after account statements are issued, teams may have weeks to detect and correct issues before customers notice. Time is the most underappreciated risk control in large transformations.

### 5. Align the Right Team for Cutover Night
The team that builds the system is not the team that safely implements it. Cutover requires a highly specific mix of resources from Project/BAU Support and Incident Management.