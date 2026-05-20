<span class="section-label">Executive Playbooks</span>

# The Cutover Playbook: Embracing the Delta

> *"Don't hope D-Day will be Blue Skies... Be paranoid in the lead-up in a good way. That's how you earn a good night's sleep and wake up confident and full of energy on D-Day."*

**Production Reality:** Testing will never fully replicate production. That is not a failure of capability — it is a structural reality. No matter how mature the test environment or how seasoned the QA team, certain failure modes only become visible for the first time after go-live. The real exposure often sits below the application layer — system-level settings, runtime parameters, and environmental conditions that no test can faithfully replicate.

Effective risk management begins by acknowledging the delta rather than attempting to eliminate it. The objective is to identify where failure is plausible, and design containment before impact becomes material.

---

## The Cutover Failure Equation

<div class="ceq-wrapper">

  <div class="ceq-intro">
    <p class="ceq-formula-text">Failure Impact &nbsp;=&nbsp; Detection Delay &nbsp;&times;&nbsp; Decision Delay &nbsp;&times;&nbsp; Execution Delay</p>
    <p class="ceq-tagline">Minimising any single delay factor reduces overall failure impact exponentially</p>
  </div>

  <!-- Formula boxes -->
  <div class="ceq-boxes">
    <div class="ceq-box ceq-box-detect">
      <div class="ceq-box-title">Detection<br>Delay</div>
      <div class="ceq-box-sub">Time to identify and understand the problem</div>
    </div>
    <div class="ceq-operator">&times;</div>
    <div class="ceq-box ceq-box-decide">
      <div class="ceq-box-title">Decision<br>Delay</div>
      <div class="ceq-box-sub">Time to decide on containment then recovery path</div>
    </div>
    <div class="ceq-operator">&times;</div>
    <div class="ceq-box ceq-box-execute">
      <div class="ceq-box-title">Execution<br>Delay</div>
      <div class="ceq-box-sub">Time to implement the fix and validate</div>
    </div>
    <div class="ceq-operator">=</div>
    <div class="ceq-box ceq-box-impact">
      <div class="ceq-box-title">FAILURE<br>IMPACT</div>
      <div class="ceq-box-sub">Total business impact</div>
    </div>
  </div>

  <!-- Columns -->
  <div class="ceq-columns">

    <!-- Column 1: Detection -->
    <div class="ceq-col ceq-col-detect">
      <div class="ceq-col-time">~60 min</div>
      <div class="ceq-col-header">Detect &amp; Triage</div>
      <ul class="ceq-list">
        <li>Failure mode understood?</li>
        <li>Are we making it worse?</li>
        <li>What are the downstream dependencies?</li>
        <li>Is there a time-sensitive business deadline?</li>
        <li>What signals confirm the scope of impact?</li>
        <li>Do we have enough to stop, isolate, or contain?</li>
        <li>Is rollback still possible?</li>
      </ul>
    </div>

    <!-- Columns 2+3: Decision Delay group with bracket -->
    <div class="ceq-decision-group">
      <div class="ceq-decision-bracket">Decision Delay</div>
      <div class="ceq-decision-inner">

        <!-- Column 2: Containment Decision -->
        <div class="ceq-col ceq-col-contain">
          <div class="ceq-col-time">~20–30 min</div>
          <div class="ceq-col-header">Containment Decision</div>
          <div class="ceq-badge">Immediate</div>
          <p class="ceq-col-note">What do we do right now to stop the bleeding? Options depend on context — there is rarely one right answer.</p>
          <ul class="ceq-list">
            <li>Throttle traffic</li>
            <li>Fail over regions</li>
            <li>Switch to read-only</li>
            <li>Isolate impacted customers</li>
            <li>Stop background jobs</li>
            <li>Disable integrations</li>
            <li>Pause queues &amp; processors</li>
            <li>Prevent bad data spread</li>
            <li>Reduce functionality temporarily</li>
          </ul>
        </div>

        <!-- Column 3: Recovery Decision -->
        <div class="ceq-col ceq-col-recover">
          <div class="ceq-col-time">~60–90 min</div>
          <div class="ceq-col-header">Recovery Decision</div>
          <p class="ceq-col-note">Containment has bought you time. Now choose the safest path forward with the information available.</p>
          <ul class="ceq-list">
            <li>Rollback or fix forward?</li>
            <li>Partial service or full outage?</li>
            <li>Risk profile of each path?</li>
            <li>Can we avoid making it worse?</li>
            <li>Critical business deadlines?</li>
            <li>Impacted dependencies?</li>
            <li>Interim fix to restore service?</li>
            <li>What assurance can we give the business?</li>
          </ul>
        </div>

      </div>
    </div>

    <!-- Column 4: Execute & Validate -->
    <div class="ceq-col ceq-col-execute">
      <div class="ceq-col-time">Parallel</div>
      <div class="ceq-col-header">Execute &amp; Validate</div>

      <div class="ceq-sub-section">
        <div class="ceq-sub-header">Data Integrity Checks</div>
        <ul class="ceq-list">
          <li>Was data lost or duplicated?</li>
          <li>Was data corrupted?</li>
          <li>Was processing out of order?</li>
          <li>Were downstream systems affected?</li>
          <li>Are audit logs intact?</li>
        </ul>
      </div>

      <div class="ceq-sub-section">
        <div class="ceq-sub-header">Recovery Activities</div>
        <ul class="ceq-list">
          <li>Replay events / messages</li>
          <li>Restore backups</li>
          <li>Reconcile databases</li>
          <li>Re-run failed jobs</li>
          <li>Recover missing transactions</li>
        </ul>
      </div>

      <div class="ceq-sub-section">
        <div class="ceq-sub-header">Validation</div>
        <ul class="ceq-list">
          <li>Reconciliation reports</li>
          <li>Checksum / count validation</li>
          <li>Customer verification</li>
          <li>Financial reconciliation</li>
          <li>Business &amp; data owner sign-off</li>
        </ul>
      </div>

      <div class="ceq-integrity-note">
        Recovery is not complete until data integrity is verified
      </div>
    </div>

  </div>

  <!-- Timing bar -->
  <div class="ceq-timing-bar">
    <span class="ceq-timing-label">Best case total window:</span>
    <span class="ceq-timing-value">3–4 hours — from failure to recovery</span>
  </div>

</div>

---

## The Two Critical Risk Parameters

<div class="card-grid">
  <div class="card">
    <h3>Impact Latency Window (ILW)</h3>
    <p>The time between when a defect occurs and when a customer or regulator becomes aware of it. Maximising this window gives the team room to detect and contain before exposure becomes material.</p>
  </div>
  <div class="card">
    <h3>Impact Amplification Window (IAW)</h3>
    <p>The point at which an isolated defect begins to compound into widespread operational, financial, or reputational damage. Containment strategies must activate before this threshold is crossed.</p>
  </div>
</div>

---

## The Five Principles of Cutover

<div class="principle">
<h3>1. Focus on the Grey Areas</h3>
Start with what cannot be evaluated faithfully in QA. Where production conditions diverge, documentation becomes less dependable and experience becomes critical. These are the zones where surprises emerge. Test coverage metrics alone are not a proxy for safety.
</div>

<div class="principle">
<h3>2. Prioritise Risk with Objective Scoring</h3>
Intuition has limits, especially under deadline pressure. A structured framework such as Failure Mode and Effects Analysis (FMEA) imposes discipline: assess severity, likelihood, and detectability, then rank exposures accordingly. Prioritisation is a strategy.
</div>

<div class="principle">
<h3>3. Reduce Customer Exposure</h3>
Containment begins with volume control. The critical question is simple: must every transaction file be processed immediately, or can exposure be deliberately constrained? Reducing exposure converts potential crises into manageable operational issues.
</div>

<div class="principle">
<h3>4. Maximise the Impact Latency Window</h3>
Timing decisions are often treated as logistical details. They are strategic controls. If a cutover occurs just after account statements are issued, teams may have weeks to detect and correct issues before customers notice. Time is the most underappreciated risk control in large transformations.
</div>

<div class="principle">
<h3>5. Align the Right Team for Cutover Night</h3>
The team that builds the system is not the team that safely runs the cutover. Cutover night requires people who have lived through production crises — who carry historical memory, recognise failure patterns, know containment tactics, and can make calculated decisions when only 80% of the information is available.
</div>
