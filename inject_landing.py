NEW_LOGIN = r'''<div id="dim"></div>

<!-- ═══════════════════════════════════════════════════════════
     LANDING PAGE  –  Crew Health Console
     NASA Space Apps Challenge · Palestine
═══════════════════════════════════════════════════════════ -->
<div id="login">

<!-- ── STICKY TOP-BAR ──────────────────────────────────────── -->
<nav id="lp-nav" aria-label="Landing page navigation">
  <div class="lp-nav-inner">
    <div class="lp-logo-row">
      <img src="nasa_logo.png" alt="NASA" class="lp-nasa-logo">
      <span class="lp-brand-name">Crew Health Console</span>
    </div>
    <div class="lp-nav-links" role="list">
      <a href="#lp-problem" role="listitem" data-en="Problem" data-ar="المشكلة">Problem</a>
      <a href="#lp-solution" role="listitem" data-en="Solution" data-ar="الحل">Solution</a>
      <a href="#lp-team" role="listitem" data-en="Team" data-ar="الفريق">Team</a>
      <a href="#lp-signin" role="listitem" data-en="Sign in" data-ar="تسجيل الدخول">Sign in</a>
    </div>
    <div class="lp-nav-controls">
      <button class="thm btn-util lp-util" id="lpThm" title="Toggle theme" aria-label="Toggle theme"></button>
      <button class="btn-util lp-util lp-lang" id="lpLang" title="Switch language" aria-label="Switch language">عربي</button>
      <a href="#lp-signin" class="lp-cta-btn" data-en="Start session" data-ar="ابدأ الجلسة">Start session</a>
    </div>
  </div>
</nav>

<!-- ── HERO ────────────────────────────────────────────────── -->
<section id="lp-hero" aria-labelledby="lp-hero-h1">
  <div class="lp-stars" aria-hidden="true">
    <span></span><span></span><span></span><span></span><span></span>
    <span></span><span></span><span></span><span></span><span></span>
    <span></span><span></span><span></span><span></span><span></span>
    <span></span><span></span><span></span><span></span><span></span>
  </div>
  <div class="lp-hero-inner">
    <div class="lp-hero-content">
      <span class="lp-challenge-badge" data-en="Built for NASA Space Apps Challenge &bull; Palestine 2024" data-ar="مبني لتحدي ناسا للتطبيقات الفضائية &bull; فلسطين 2024">Built for NASA Space Apps Challenge &bull; Palestine 2024</span>
      <h1 id="lp-hero-h1" data-en="Crew Health Console" data-ar="لوحة صحة الطاقم">Crew Health Console</h1>
      <p class="lp-tagline" data-en="Personal health monitoring and mental wellbeing for astronauts, far from Earth." data-ar="مراقبة الصحة الشخصية والرفاهية النفسية لرواد الفضاء، بعيداً عن الأرض.">Personal health monitoring and mental wellbeing for astronauts, far from Earth.</p>
      <div class="lp-hero-btns">
        <a href="#lp-signin" class="lp-btn-primary" data-en="Start your session" data-ar="ابدأ جلستك">Start your session</a>
        <a href="#lp-problem" class="lp-btn-ghost" data-en="Learn more" data-ar="اعرف أكثر">Learn more</a>
      </div>
    </div>
    <div class="lp-hero-visual" aria-hidden="true">
      <div class="lp-hud-frame">
        <img src="human_figure.png" alt="" class="lp-body-preview">
        <div class="lp-hud-pulse"></div>
        <div class="lp-hud-label lp-hud-tl">HR: 68 bpm</div>
        <div class="lp-hud-label lp-hud-tr">SpO&#8322;: 97%</div>
        <div class="lp-hud-label lp-hud-bl">Temp: 36.7°C</div>
        <div class="lp-hud-label lp-hud-br">BP: 118/76</div>
        <svg class="lp-ecg-mini" viewBox="0 0 200 40" aria-hidden="true">
          <path d="M0 20 l12 0 l5 -8 l5 8 l5 0 l3 5 l4 -28 l4 32 l3 -9 l8 0 l5 -8 l5 8 l5 0 l3 5 l4 -28 l4 32 l3 -9 l8 0 l5 -8 l5 8 l5 0 l3 5 l4 -28 l4 32 l3 -9 l30 0" fill="none" stroke="var(--acc)" stroke-width="1.5" class="lp-ecg-path"/>
        </svg>
      </div>
    </div>
  </div>
  <a href="#lp-problem" class="lp-scroll-cue" aria-label="Scroll to problem section">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg>
  </a>
</section>

<!-- ── THE PROBLEM ─────────────────────────────────────────── -->
<section id="lp-problem" class="lp-section" aria-labelledby="lp-prob-h2">
  <div class="lp-section-inner">
    <div class="lp-section-label" data-en="The Challenge" data-ar="التحدي">The Challenge</div>
    <h2 id="lp-prob-h2" data-en="Astronauts manage their health alone, millions of miles from any doctor." data-ar="رواد الفضاء يديرون صحتهم بمفردهم، على بُعد ملايين الأميال من أي طبيب.">Astronauts manage their health alone, millions of miles from any doctor.</h2>
    <p class="lp-lead" data-en="On the Moon and Mars, messages to Earth take many minutes each way. Crews must detect problems early, understand what they mean, and act on their own." data-ar="على القمر والمريخ، تستغرق الرسائل إلى الأرض دقائق طويلة في كلا الاتجاهين. يجب على الأطقم اكتشاف المشاكل مبكراً وفهم ما تعنيه والتصرف بمفردهم.">On the Moon and Mars, messages to Earth take many minutes each way. Crews must detect problems early, understand what they mean, and act on their own.</p>
    <div class="lp-problem-cards" role="list">
      <div class="lp-prob-card" role="listitem">
        <div class="lp-prob-icon" style="color:#ef4444">&#9762;</div>
        <div class="lp-prob-text"><strong data-en="Radiation" data-ar="الإشعاع">Radiation</strong><span data-en="Invisible high-energy particles that raise long-term cancer risk and damage the nervous system." data-ar="جسيمات عالية الطاقة غير مرئية ترفع خطر السرطان على المدى البعيد وتضر بالجهاز العصبي.">Invisible high-energy particles that raise long-term cancer risk and damage the nervous system.</span></div>
      </div>
      <div class="lp-prob-card" role="listitem">
        <div class="lp-prob-icon" style="color:#f59e0b">&#9881;</div>
        <div class="lp-prob-text"><strong data-en="Bone &amp; Muscle Loss" data-ar="فقدان العظام والعضلات">Bone &amp; Muscle Loss</strong><span data-en="Without gravity, bones shed density and muscles shrink rapidly in microgravity." data-ar="بدون الجاذبية، تفقد العظام كثافتها وتتقلص العضلات بسرعة في انعدام الوزن.">Without gravity, bones shed density and muscles shrink rapidly in microgravity.</span></div>
      </div>
      <div class="lp-prob-card" role="listitem">
        <div class="lp-prob-icon" style="color:#a78bfa">&#10084;</div>
        <div class="lp-prob-text"><strong data-en="Cardiovascular Changes" data-ar="تغيرات القلب والأوعية">Cardiovascular Changes</strong><span data-en="Fluid shifts alter heart function, vision, blood pressure, and balance." data-ar="انتقالات السوائل تغير وظيفة القلب والرؤية وضغط الدم والتوازن.">Fluid shifts alter heart function, vision, blood pressure, and balance.</span></div>
      </div>
      <div class="lp-prob-card" role="listitem">
        <div class="lp-prob-icon" style="color:#60a5fa">&#9790;</div>
        <div class="lp-prob-text"><strong data-en="Sleep Disruption" data-ar="اضطراب النوم">Sleep Disruption</strong><span data-en="Microgravity and 16 sunrises per day destroy the circadian rhythm." data-ar="انعدام الجاذبية و16 شروقاً للشمس يومياً يدمران إيقاع الساعة البيولوجية.">Microgravity and 16 sunrises per day destroy the circadian rhythm.</span></div>
      </div>
      <div class="lp-prob-card" role="listitem">
        <div class="lp-prob-icon" style="color:#34d399">&#128100;</div>
        <div class="lp-prob-text"><strong data-en="Isolation &amp; Stress" data-ar="العزلة والتوتر">Isolation &amp; Stress</strong><span data-en="Months of confinement with the same small crew affects mood, cognition, and teamwork." data-ar="أشهر من العزل مع نفس الطاقم الصغير يؤثر على المزاج والإدراك والعمل الجماعي.">Months of confinement with the same small crew affects mood, cognition, and teamwork.</span></div>
      </div>
      <div class="lp-prob-card" role="listitem">
        <div class="lp-prob-icon" style="color:#fb923c">&#127783;</div>
        <div class="lp-prob-text"><strong data-en="Cabin Environment" data-ar="بيئة المركبة">Cabin Environment</strong><span data-en="CO&#8322; build-up, pressure leaks, particulates, and noise all impact health silently." data-ar="تراكم ثاني أكسيد الكربون وتسربات الضغط والجسيمات والضجيج تؤثر جميعها على الصحة بصمت.">CO&#8322; build-up, pressure leaks, particulates, and noise all impact health silently.</span></div>
      </div>
    </div>
  </div>
</section>

<!-- ── THE SOLUTION ────────────────────────────────────────── -->
<section id="lp-solution" class="lp-section lp-alt" aria-labelledby="lp-sol-h2">
  <div class="lp-section-inner">
    <div class="lp-section-label" data-en="Our Approach" data-ar="نهجنا">Our Approach</div>
    <h2 id="lp-sol-h2" data-en="A complete health companion built for the challenges of deep space." data-ar="رفيق صحي متكامل مبني لتحديات الفضاء السحيق.">A complete health companion built for the challenges of deep space.</h2>

    <div class="lp-flow" aria-label="How it works" role="list">
      <div class="lp-flow-step" role="listitem">
        <div class="lp-flow-icon">&#128200;</div>
        <div class="lp-flow-label" data-en="Measure" data-ar="قِس">Measure</div>
      </div>
      <div class="lp-flow-arrow" aria-hidden="true">&#8594;</div>
      <div class="lp-flow-step" role="listitem">
        <div class="lp-flow-icon">&#129504;</div>
        <div class="lp-flow-label" data-en="Understand" data-ar="افهم">Understand</div>
      </div>
      <div class="lp-flow-arrow" aria-hidden="true">&#8594;</div>
      <div class="lp-flow-step" role="listitem">
        <div class="lp-flow-icon">&#128276;</div>
        <div class="lp-flow-label" data-en="Alert" data-ar="نبّه">Alert</div>
      </div>
      <div class="lp-flow-arrow" aria-hidden="true">&#8594;</div>
      <div class="lp-flow-step" role="listitem">
        <div class="lp-flow-icon">&#128149;</div>
        <div class="lp-flow-label" data-en="Recover" data-ar="تعافَ">Recover</div>
      </div>
    </div>

    <div class="lp-features" role="list">
      <div class="lp-feat" role="listitem">
        <div class="lp-feat-icon">&#128100;</div>
        <div><strong data-en="Personal Profile" data-ar="الملف الشخصي">Personal Profile</strong><p data-en="Readings and triage are tailored to your blood type, sex, genetic notes, and mission location." data-ar="تُخصَّص القراءات والفرز الطبي وفقاً لفصيلة دمك وجنسك وملاحظاتك الجينية وموقع مهمتك.">Readings and triage are tailored to your blood type, sex, genetic notes, and mission location.</p></div>
      </div>
      <div class="lp-feat" role="listitem">
        <div class="lp-feat-icon">&#129507;</div>
        <div><strong data-en="Interactive Body Map" data-ar="خريطة الجسم التفاعلية">Interactive Body Map</strong><p data-en="Tap any body region to see active alerts and every spaceflight risk for that system." data-ar="اضغط على أي منطقة من الجسم لرؤية التنبيهات النشطة وكل مخاطر رحلات الفضاء لذلك الجهاز.">Tap any body region to see active alerts and every spaceflight risk for that system.</p></div>
      </div>
      <div class="lp-feat" role="listitem">
        <div class="lp-feat-icon">&#128200;</div>
        <div><strong data-en="Daily Check-ins" data-ar="تسجيلات يومية">Daily Check-ins</strong><p data-en="Log mood, sleep, food, water, exercise, heart rate, blood pressure, oxygen, glucose, and temperature." data-ar="سجّل المزاج والنوم والطعام والماء والتمارين ومعدل ضربات القلب وضغط الدم والأكسجين والجلوكوز ودرجة الحرارة.">Log mood, sleep, food, water, exercise, heart rate, blood pressure, oxygen, glucose, and temperature.</p></div>
      </div>
      <div class="lp-feat" role="listitem">
        <div class="lp-feat-icon">&#128203;</div>
        <div><strong data-en="Symptom Triage" data-ar="فرز الأعراض">Symptom Triage</strong><p data-en="Describe a symptom in plain words and attach a photo to get rule-based guidance and AI analysis." data-ar="صِف العَرَض بكلمات بسيطة وأرفق صورة للحصول على إرشادات مبنية على قواعد وتحليل ذكاء اصطناعي.">Describe a symptom in plain words and attach a photo to get rule-based guidance and AI analysis.</p></div>
      </div>
      <div class="lp-feat" role="listitem">
        <div class="lp-feat-icon">&#128268;</div>
        <div><strong data-en="Live Environment Sensors" data-ar="مستشعرات البيئة الحية">Live Environment Sensors</strong><p data-en="Real-time CO&#8322;, O&#8322;, pressure, humidity, particulates, and radiation feeds with zone alerts." data-ar="بيانات حية للـCO₂ والأكسجين والضغط والرطوبة والجسيمات والإشعاع مع تنبيهات منطقية.">Real-time CO&#8322;, O&#8322;, pressure, humidity, particulates, and radiation feeds with zone alerts.</p></div>
      </div>
      <div class="lp-feat" role="listitem">
        <div class="lp-feat-icon">&#128680;</div>
        <div><strong data-en="Emergency Notification" data-ar="إشعار الطوارئ">Emergency Notification</strong><p data-en="Critical events instantly alert the flight surgeon, medical officer, commander, and flight director." data-ar="الأحداث الحرجة تنبّه فوراً الجراح الطائر والضابط الطبي والقائد ومدير الرحلة.">Critical events instantly alert the flight surgeon, medical officer, commander, and flight director.</p></div>
      </div>
      <div class="lp-feat" role="listitem">
        <div class="lp-feat-icon">&#128218;</div>
        <div><strong data-en="NASA Risk Watch" data-ar="مراقبة مخاطر ناسا">NASA Risk Watch</strong><p data-en="Tracks the five major spaceflight hazards and 30 risks from NASA's Human Research Program." data-ar="تتبّع المخاطر الخمس الرئيسية لرحلات الفضاء و30 خطراً من برنامج أبحاث الإنسان التابع لناسا.">Tracks the five major spaceflight hazards and 30 risks from NASA's Human Research Program.</p></div>
      </div>
      <div class="lp-feat" role="listitem">
        <div class="lp-feat-icon">&#127918;</div>
        <div><strong data-en="Motor &amp; Memory Tests" data-ar="اختبارات الحركة والذاكرة">Motor &amp; Memory Tests</strong><p data-en="Asteroid intercept and pattern-recall games track reaction time and cognitive performance over time." data-ar="ألعاب اعتراض الكويكبات واستدعاء الأنماط تتبّع وقت الاستجابة والأداء المعرفي بمرور الوقت.">Asteroid intercept and pattern-recall games track reaction time and cognitive performance over time.</p></div>
      </div>
      <div class="lp-feat" role="listitem">
        <div class="lp-feat-icon">&#127795;</div>
        <div><strong data-en="VR Earth Sanctuary" data-ar="ملاذ الأرض الافتراضي">VR Earth Sanctuary</strong><p data-en="A personal calming biome from home — forest, lake, ocean, or meadow — with ambient soundscape and breathing guide." data-ar="بيئة هادئة شخصية من الوطن - غابة أو بحيرة أو محيط أو مرج - مع مشهد صوتي محيطي ودليل تنفس.">A personal calming biome from home — forest, lake, ocean, or meadow — with ambient soundscape and breathing guide.</p></div>
      </div>
    </div>
  </div>
</section>

<!-- ── TEAM ─────────────────────────────────────────────────── -->
<section id="lp-team" class="lp-section" aria-labelledby="lp-team-h2">
  <div class="lp-section-inner">
    <div class="lp-section-label" data-en="The Team" data-ar="الفريق">The Team</div>
    <h2 id="lp-team-h2" data-en="Meet the builders" data-ar="تعرف على الفريق">Meet the builders</h2>
    <p class="lp-lead" data-en="A team from Palestine who built this project during the NASA Space Apps Challenge." data-ar="فريق من فلسطين بنى هذا المشروع خلال تحدي ناسا للتطبيقات الفضائية.">A team from Palestine who built this project during the NASA Space Apps Challenge.</p>
    <div class="lp-team-grid" role="list">
      <!-- Edit the data-role attribute on each card to update member roles -->
      <div class="lp-member" role="listitem" data-role="Project Lead &amp; Full-Stack Developer">
        <div class="lp-avatar" aria-hidden="true"><span>A</span></div>
        <div class="lp-member-name">Amr</div>
        <div class="lp-member-role">Project Lead &amp; Full-Stack Developer</div>
      </div>
      <div class="lp-member" role="listitem" data-role="Health Data Systems">
        <div class="lp-avatar" aria-hidden="true"><span>M</span></div>
        <div class="lp-member-name">Mojahid</div>
        <div class="lp-member-role">Health Data Systems</div>
      </div>
      <div class="lp-member" role="listitem" data-role="UI/UX Designer">
        <div class="lp-avatar" aria-hidden="true"><span>A</span></div>
        <div class="lp-member-name">Ahmad</div>
        <div class="lp-member-role">UI/UX Designer</div>
      </div>
      <div class="lp-member" role="listitem" data-role="Biomedical Research">
        <div class="lp-avatar" aria-hidden="true"><span>A</span></div>
        <div class="lp-member-name">Abdulrahman</div>
        <div class="lp-member-role">Biomedical Research</div>
      </div>
      <div class="lp-member" role="listitem" data-role="Sensor &amp; Environment Systems">
        <div class="lp-avatar" aria-hidden="true"><span>H</span></div>
        <div class="lp-member-name">Hothayfa</div>
        <div class="lp-member-role">Sensor &amp; Environment Systems</div>
      </div>
      <div class="lp-member" role="listitem" data-role="VR &amp; Mental Health Module">
        <div class="lp-avatar" aria-hidden="true"><span>M</span></div>
        <div class="lp-member-name">Mohammad</div>
        <div class="lp-member-role">VR &amp; Mental Health Module</div>
      </div>
    </div>
  </div>
</section>

<!-- ── ABOUT THE CHALLENGE ─────────────────────────────────── -->
<section id="lp-about" class="lp-section lp-alt" aria-labelledby="lp-about-h2">
  <div class="lp-section-inner lp-about-inner">
    <div>
      <div class="lp-section-label" data-en="About the Challenge" data-ar="عن التحدي">About the Challenge</div>
      <h2 id="lp-about-h2" data-en="NASA International Space Apps Challenge" data-ar="تحدي ناسا الدولي للتطبيقات الفضائية">NASA International Space Apps Challenge</h2>
      <p data-en="The NASA Space Apps Challenge is the world's largest global hackathon, running in more than 150 countries. This project was built during the 2024 edition through the Palestine chapter, responding to the open challenge of supporting astronaut health in deep space." data-ar="تحدي ناسا للتطبيقات الفضائية هو أكبر هاكاثون عالمي في العالم، يُقام في أكثر من 150 دولة. تم بناء هذا المشروع خلال النسخة 2024 من خلال فرع فلسطين، استجابةً لتحدي دعم صحة رواد الفضاء في الفضاء السحيق.">The NASA Space Apps Challenge is the world's largest global hackathon, running in more than 150 countries. This project was built during the 2024 edition through the Palestine chapter, responding to the open challenge of supporting astronaut health in deep space.</p>
      <div class="lp-challenge-info">
        <!-- Edit this line to update the challenge name and year -->
        <strong data-en="Challenge:" data-ar="التحدي:">Challenge:</strong>
        <span data-en="Maintaining Astronaut Health: Monitoring and Safeguarding Crew Wellbeing" data-ar="الحفاظ على صحة رواد الفضاء: مراقبة وصون رفاهية الطاقم">Maintaining Astronaut Health: Monitoring and Safeguarding Crew Wellbeing</span>
        <strong data-en="Year:" data-ar="السنة:">Year:</strong>
        <span>2024</span>
      </div>
      <div class="lp-nasa-links" style="margin-top:16px">
        <a href="https://www.nasa.gov/hrp/hazards/" target="_blank" rel="noopener" data-en="NASA Spaceflight Hazards" data-ar="مخاطر رحلات الفضاء - ناسا">NASA Spaceflight Hazards</a>
        <a href="https://www.nasa.gov/hrp/risks/" target="_blank" rel="noopener" data-en="NASA HRP Risks" data-ar="مخاطر برنامج أبحاث الإنسان - ناسا">NASA HRP Risks</a>
      </div>
    </div>
    <div class="lp-about-visual" aria-hidden="true">
      <img src="nasa_logo.png" alt="" class="lp-about-logo">
      <div class="lp-flag-badge">&#127477;&#127480;</div>
    </div>
  </div>
</section>

<!-- ── SIGN-IN FORM ─────────────────────────────────────────── -->
<section id="lp-signin" class="lp-section" aria-labelledby="lp-signin-h2">
  <div class="lp-section-inner">
    <div class="lp-section-label" data-en="Profile Setup" data-ar="إعداد الملف الشخصي">Profile Setup</div>
    <h2 id="lp-signin-h2" data-en="Start your session" data-ar="ابدأ جلستك">Start your session</h2>
    <p class="lp-lead" data-en="Your profile shapes how the console interprets your readings. All data stays in your browser — nothing is sent to a server." data-ar="ملفك الشخصي يحدد كيفية تفسير اللوحة لقراءاتك. جميع البيانات تبقى في متصفحك - لا شيء يُرسَل إلى خادم.">Your profile shapes how the console interprets your readings. All data stays in your browser — nothing is sent to a server.</p>
    <div class="lp-form-panel panel">
      <div class="lp-form-grid">
        <div class="lp-form-col">
          <label for="lName" data-en="Full name" data-ar="الاسم الكامل">Full name</label>
          <input type="text" id="lName" placeholder="e.g. Cdr. A. Rahman" autocomplete="name">
          <label for="lBlood" data-en="Blood type" data-ar="فصيلة الدم">Blood type</label>
          <select id="lBlood">
            <option>O+</option><option>O−</option><option>A+</option><option>A−</option>
            <option>B+</option><option>B−</option><option>AB+</option><option>AB−</option>
          </select>
          <label for="lSex" data-en="Sex" data-ar="الجنس">Sex</label>
          <select id="lSex">
            <option data-en="Female" data-ar="أنثى">Female</option>
            <option data-en="Male" data-ar="ذكر">Male</option>
            <option data-en="Other" data-ar="آخر">Other</option>
          </select>
        </div>
        <div class="lp-form-col">
          <label for="lGene" data-en="Genetic notes" data-ar="الملاحظات الجينية">Genetic notes</label>
          <input type="text" id="lGene" placeholder="e.g. sickle cell trait, family history of heart disease">
          <label for="lEnv" data-en="Current location" data-ar="الموقع الحالي">Current location</label>
          <select id="lEnv">
            <option data-en="International Space Station" data-ar="محطة الفضاء الدولية">International Space Station</option>
            <option data-en="Spacecraft in transit" data-ar="مركبة فضائية في العبور">Spacecraft in transit</option>
            <option data-en="Lunar base" data-ar="قاعدة قمرية">Lunar base</option>
            <option data-en="Mars base" data-ar="قاعدة مريخية">Mars base</option>
            <option data-en="Lunar rover" data-ar="مركبة قمرية">Lunar rover</option>
            <option data-en="Mars rover" data-ar="مركبة مريخية">Mars rover</option>
          </select>
          <label for="lSanctuary" data-en="Earth Sanctuary (Personal VR Happy Place)" data-ar="ملاذ الأرض (مكانك السعيد الافتراضي)">Earth Sanctuary (Personal VR Happy Place)</label>
          <select id="lSanctuary">
            <option value="forest" data-en="Pine Forest &amp; Mountain Trail" data-ar="غابة الصنوبر ومسار الجبل">Pine Forest &amp; Mountain Trail</option>
            <option value="lake" data-en="Alpine Lake at Sunrise" data-ar="البحيرة الجبلية عند الشروق">Alpine Lake at Sunrise</option>
            <option value="ocean" data-en="Pacific Ocean Coastline" data-ar="ساحل المحيط الهادئ">Pacific Ocean Coastline</option>
            <option value="meadow" data-en="Autumn Highland Meadow" data-ar="مرج المرتفعات في الخريف">Autumn Highland Meadow</option>
          </select>
        </div>
      </div>
      <button class="pri lp-start-btn" id="go" data-en="Launch Crew Health Console" data-ar="تشغيل لوحة صحة الطاقم">Launch Crew Health Console</button>
      <p class="mut lp-form-note" data-en="A 12-day sample flight history is preloaded. All data is stored locally in your browser and never transmitted." data-ar="يتم تحميل سجل رحلة نموذجي لمدة 12 يوماً مسبقاً. جميع البيانات مخزنة محلياً في متصفحك ولا تُرسَل أبداً.">A 12-day sample flight history is preloaded. All data is stored locally in your browser and never transmitted.</p>
    </div>
  </div>
</section>

<!-- ── FOOTER ───────────────────────────────────────────────── -->
<footer class="lp-footer" role="contentinfo">
  <div class="lp-section-inner lp-footer-inner">
    <div class="lp-footer-brand">
      <img src="nasa_logo.png" alt="NASA" style="height:28px;vertical-align:middle;margin-right:8px">
      <span class="lp-footer-title">Crew Health Console</span>
    </div>
    <p class="lp-disclaimer" data-en="This is a student-built prototype for a hackathon. It is not medical advice and is not an official NASA product. Always follow your flight surgeon's protocol." data-ar="هذا نموذج أولي من بناء الطلاب لهاكاثون. إنه ليس نصيحة طبية وليس منتجاً رسمياً لناسا. اتبع دائماً بروتوكول جراحك الطائر.">This is a student-built prototype for a hackathon. It is not medical advice and is not an official NASA product. Always follow your flight surgeon's protocol.</p>
    <div class="lp-footer-links">
      <a href="https://www.nasa.gov/hrp/hazards/" target="_blank" rel="noopener">NASA Hazards</a>
      <a href="https://www.nasa.gov/hrp/risks/" target="_blank" rel="noopener">NASA HRP Risks</a>
      <a href="https://www.spaceappschallenge.org/" target="_blank" rel="noopener">Space Apps Challenge</a>
    </div>
    <p class="lp-footer-copy">&copy; 2024 Palestine Space Apps Team</p>
  </div>
</footer>

</div><!-- end #login -->
'''

LANDING_CSS = r'''
/* ═══════════════════════════════════════════════════════════
   LANDING PAGE STYLES
═══════════════════════════════════════════════════════════ */

/* ── Layout reset for landing ── */
#login {
  min-height: 100vh;
  background: var(--bg);
  font-family: inherit;
  scroll-behavior: smooth;
  overflow-x: hidden;
}

/* ── Top Nav ── */
#lp-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--panel);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--line);
  box-shadow: 0 2px 20px rgba(0,0,0,0.15);
}
.lp-nav-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 10px 24px;
  max-width: 1200px;
  margin: 0 auto;
  flex-wrap: wrap;
}
.lp-logo-row {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}
.lp-nasa-logo {
  height: 30px;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(0 2px 6px rgba(0,0,0,0.3));
}
.lp-brand-name {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--ink);
  white-space: nowrap;
  letter-spacing: -0.01em;
}
.lp-nav-links {
  display: flex;
  gap: 4px;
  align-items: center;
}
.lp-nav-links a {
  color: var(--mut);
  text-decoration: none;
  font-size: 0.82rem;
  font-weight: 600;
  padding: 5px 12px;
  border-radius: var(--radius-full);
  transition: color 0.2s, background 0.2s;
  letter-spacing: 0.01em;
}
.lp-nav-links a:hover, .lp-nav-links a:focus-visible {
  color: var(--ink);
  background: var(--surface-glass);
  outline: none;
}
.lp-nav-controls {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-shrink: 0;
}
.lp-util {
  font-size: 0.78rem;
  padding: 5px 10px;
}
.lp-lang {
  font-family: 'Segoe UI', system-ui, sans-serif;
  font-weight: 700;
  letter-spacing: 0;
}
.lp-cta-btn {
  display: inline-block;
  background: var(--acc-grad);
  color: #fff;
  font-size: 0.82rem;
  font-weight: 700;
  padding: 7px 16px;
  border-radius: var(--radius-full);
  text-decoration: none;
  transition: opacity 0.2s, transform 0.2s;
  white-space: nowrap;
  letter-spacing: 0.02em;
}
.lp-cta-btn:hover { opacity: 0.88; transform: translateY(-1px); }

/* ── Stars canvas ── */
#lp-hero {
  position: relative;
  min-height: 92vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding: 60px 24px 40px;
}
.lp-stars {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
}
.lp-stars span {
  position: absolute;
  display: block;
  border-radius: 50%;
  background: white;
  opacity: 0;
  animation: lp-twinkle linear infinite;
}
.lp-stars span:nth-child(1)  { width:2px;height:2px;top:8%;left:12%;animation-duration:3.1s;animation-delay:0.2s; }
.lp-stars span:nth-child(2)  { width:1px;height:1px;top:15%;left:72%;animation-duration:4.2s;animation-delay:1.1s; }
.lp-stars span:nth-child(3)  { width:3px;height:3px;top:22%;left:35%;animation-duration:2.8s;animation-delay:0.6s; }
.lp-stars span:nth-child(4)  { width:1px;height:1px;top:30%;left:88%;animation-duration:3.7s;animation-delay:1.5s; }
.lp-stars span:nth-child(5)  { width:2px;height:2px;top:42%;left:5%;animation-duration:5.1s;animation-delay:0.3s; }
.lp-stars span:nth-child(6)  { width:1px;height:1px;top:55%;left:60%;animation-duration:3.4s;animation-delay:2.1s; }
.lp-stars span:nth-child(7)  { width:2px;height:2px;top:65%;left:25%;animation-duration:4.0s;animation-delay:0.9s; }
.lp-stars span:nth-child(8)  { width:1px;height:1px;top:75%;left:80%;animation-duration:2.6s;animation-delay:1.7s; }
.lp-stars span:nth-child(9)  { width:3px;height:3px;top:88%;left:45%;animation-duration:3.9s;animation-delay:0.4s; }
.lp-stars span:nth-child(10) { width:1px;height:1px;top:5%;left:55%;animation-duration:4.5s;animation-delay:2.4s; }
.lp-stars span:nth-child(11) { width:2px;height:2px;top:18%;left:92%;animation-duration:3.2s;animation-delay:1.0s; }
.lp-stars span:nth-child(12) { width:1px;height:1px;top:38%;left:18%;animation-duration:5.4s;animation-delay:0.7s; }
.lp-stars span:nth-child(13) { width:2px;height:2px;top:50%;left:50%;animation-duration:2.9s;animation-delay:1.9s; }
.lp-stars span:nth-child(14) { width:1px;height:1px;top:70%;left:38%;animation-duration:4.1s;animation-delay:0.5s; }
.lp-stars span:nth-child(15) { width:3px;height:3px;top:82%;left:68%;animation-duration:3.6s;animation-delay:1.3s; }
.lp-stars span:nth-child(16) { width:1px;height:1px;top:12%;left:28%;animation-duration:4.8s;animation-delay:2.0s; }
.lp-stars span:nth-child(17) { width:2px;height:2px;top:60%;left:95%;animation-duration:3.3s;animation-delay:0.8s; }
.lp-stars span:nth-child(18) { width:1px;height:1px;top:35%;left:75%;animation-duration:5.0s;animation-delay:1.4s; }
.lp-stars span:nth-child(19) { width:2px;height:2px;top:92%;left:15%;animation-duration:3.8s;animation-delay:2.2s; }
.lp-stars span:nth-child(20) { width:1px;height:1px;top:48%;left:42%;animation-duration:4.4s;animation-delay:0.1s; }
@keyframes lp-twinkle {
  0%,100% { opacity:0; transform:scale(0.8); }
  50% { opacity:0.9; transform:scale(1.2); }
}

/* ── Hero inner layout ── */
.lp-hero-inner {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
  max-width: 1100px;
  width: 100%;
}
.lp-hero-content { display: flex; flex-direction: column; gap: 18px; }
.lp-challenge-badge {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: var(--acc);
  background: var(--acc-glow);
  border: 1px solid rgba(0,180,216,0.3);
  padding: 4px 12px;
  border-radius: var(--radius-full);
  text-transform: uppercase;
  width: fit-content;
}
#lp-hero-h1 {
  font-size: clamp(2rem, 5vw, 3.4rem);
  font-weight: 800;
  line-height: 1.1;
  margin: 0;
  background: linear-gradient(135deg, var(--ink) 60%, var(--acc));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  letter-spacing: -0.02em;
}
.lp-tagline {
  font-size: clamp(1rem, 2vw, 1.2rem);
  color: var(--mut);
  line-height: 1.6;
  margin: 0;
}
.lp-hero-btns {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}
.lp-btn-primary {
  display: inline-block;
  background: var(--acc-grad);
  color: #fff;
  font-weight: 700;
  font-size: 0.95rem;
  padding: 12px 28px;
  border-radius: var(--radius-full);
  text-decoration: none;
  transition: opacity 0.2s, transform 0.15s;
  letter-spacing: 0.01em;
  box-shadow: 0 4px 20px var(--acc-glow);
}
.lp-btn-primary:hover { opacity: 0.88; transform: translateY(-2px); }
.lp-btn-ghost {
  display: inline-block;
  color: var(--acc);
  font-weight: 700;
  font-size: 0.95rem;
  padding: 11px 24px;
  border-radius: var(--radius-full);
  text-decoration: none;
  border: 1.5px solid var(--acc);
  transition: background 0.2s, transform 0.15s;
}
.lp-btn-ghost:hover { background: var(--acc-glow); transform: translateY(-2px); }

/* ── HUD Frame (hero visual) ── */
.lp-hero-visual { display: flex; justify-content: center; align-items: center; }
.lp-hud-frame {
  position: relative;
  width: 260px;
  height: 360px;
  border: 1px solid var(--line-strong);
  border-radius: 20px;
  background: rgba(0,180,216,0.04);
  box-shadow: 0 0 40px rgba(0,180,216,0.12), inset 0 0 20px rgba(0,180,216,0.04);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.lp-body-preview {
  height: 90%;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(0 0 16px rgba(0,180,216,0.3));
}
.lp-hud-pulse {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  animation: lp-hud-glow 3s ease-in-out infinite;
  pointer-events: none;
}
@keyframes lp-hud-glow {
  0%,100% { box-shadow: inset 0 0 20px rgba(0,180,216,0.08); }
  50%      { box-shadow: inset 0 0 40px rgba(0,180,216,0.2); }
}
.lp-hud-label {
  position: absolute;
  font-size: 0.65rem;
  font-weight: 700;
  color: var(--acc);
  background: rgba(0,180,216,0.12);
  border: 1px solid rgba(0,180,216,0.3);
  padding: 2px 7px;
  border-radius: 4px;
  letter-spacing: 0.05em;
  font-variant-numeric: tabular-nums;
}
.lp-hud-tl { top:14px;left:12px; }
.lp-hud-tr { top:14px;right:12px; }
.lp-hud-bl { bottom:48px;left:12px; }
.lp-hud-br { bottom:48px;right:12px; }
.lp-ecg-mini {
  position: absolute;
  bottom: 10px;
  left: 10px;
  right: 10px;
  height: 32px;
  width: calc(100% - 20px);
}
.lp-ecg-path {
  stroke-dasharray: 400;
  stroke-dashoffset: 400;
  animation: lp-ecg-draw 2s ease-out forwards, lp-ecg-scroll 3s linear 2s infinite;
}
@keyframes lp-ecg-draw { to { stroke-dashoffset: 0; } }
@keyframes lp-ecg-scroll { 0%,100% { opacity:1; } 90% { opacity:0.4; } }

/* ── Scroll cue ── */
.lp-scroll-cue {
  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
  color: var(--mut);
  animation: lp-bounce 2s ease-in-out infinite;
  display: block;
  z-index: 1;
}
@keyframes lp-bounce { 0%,100%{transform:translateX(-50%) translateY(0)} 50%{transform:translateX(-50%) translateY(6px)} }

/* ── Generic section wrapper ── */
.lp-section {
  padding: 80px 24px;
}
.lp-alt {
  background: rgba(255,255,255,0.02);
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}
.lp-section-inner {
  max-width: 1100px;
  margin: 0 auto;
}
.lp-section-label {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 12px;
}
.lp-section .lp-section-inner > h2 {
  font-size: clamp(1.5rem, 3.5vw, 2.3rem);
  font-weight: 800;
  margin: 0 0 20px;
  line-height: 1.2;
  letter-spacing: -0.02em;
}
.lp-lead {
  font-size: 1.05rem;
  color: var(--mut);
  line-height: 1.7;
  max-width: 700px;
  margin: 0 0 36px;
}

/* ── Problem cards ── */
.lp-problem-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
  margin-top: 12px;
}
.lp-prob-card {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 18px 20px;
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s;
}
.lp-prob-card:hover {
  border-color: var(--line-strong);
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}
.lp-prob-icon { font-size: 1.6rem; flex-shrink: 0; line-height: 1; }
.lp-prob-text { display: flex; flex-direction: column; gap: 4px; }
.lp-prob-text strong { font-size: 0.88rem; font-weight: 700; color: var(--ink); }
.lp-prob-text span { font-size: 0.82rem; color: var(--mut); line-height: 1.5; }

/* ── Solution flow ── */
.lp-flow {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 44px;
  padding: 20px 24px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
}
.lp-flow-step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  flex: 1;
  min-width: 80px;
}
.lp-flow-icon {
  font-size: 1.8rem;
  line-height: 1;
}
.lp-flow-label {
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  color: var(--ink);
}
.lp-flow-arrow {
  font-size: 1.4rem;
  color: var(--acc);
  flex-shrink: 0;
}

/* ── Feature list ── */
.lp-features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}
.lp-feat {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  padding: 18px 20px;
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  background: var(--panel);
  transition: border-color 0.2s, transform 0.2s;
}
.lp-feat:hover { border-color: var(--line-strong); transform: translateY(-2px); }
.lp-feat-icon { font-size: 1.5rem; flex-shrink: 0; line-height: 1; padding-top: 2px; }
.lp-feat strong { display: block; font-size: 0.9rem; font-weight: 700; color: var(--ink); margin-bottom: 4px; }
.lp-feat p { font-size: 0.82rem; color: var(--mut); line-height: 1.55; margin: 0; }

/* ── Team ── */
.lp-team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 20px;
  margin-top: 12px;
}
.lp-member {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  padding: 24px 16px;
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  background: var(--panel);
  text-align: center;
  transition: border-color 0.2s, box-shadow 0.2s, transform 0.2s;
}
.lp-member:hover {
  border-color: var(--acc);
  box-shadow: 0 4px 20px var(--acc-glow);
  transform: translateY(-3px);
}
.lp-avatar {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: var(--acc-grad);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  font-weight: 800;
  color: #fff;
  box-shadow: 0 4px 16px var(--acc-glow);
}
.lp-member-name { font-size: 0.95rem; font-weight: 700; color: var(--ink); }
.lp-member-role { font-size: 0.75rem; color: var(--mut); line-height: 1.4; }

/* ── About ── */
.lp-about-inner {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 48px;
  align-items: center;
}
.lp-challenge-info {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 6px 12px;
  align-items: start;
  font-size: 0.88rem;
  margin-top: 20px;
  padding: 16px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
}
.lp-challenge-info strong { color: var(--acc); font-size: 0.75rem; letter-spacing: 0.05em; text-transform: uppercase; padding-top: 2px; }
.lp-nasa-links { display: flex; gap: 12px; flex-wrap: wrap; }
.lp-nasa-links a {
  color: var(--acc);
  font-size: 0.82rem;
  font-weight: 600;
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: border-color 0.2s;
}
.lp-nasa-links a:hover { border-color: var(--acc); }
.lp-about-visual {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}
.lp-about-logo { height: 100px; width: auto; object-fit: contain; opacity: 0.85; }
.lp-flag-badge { font-size: 2.4rem; }

/* ── Sign-in form ── */
.lp-form-panel {
  margin-top: 12px;
  max-width: 820px;
}
.lp-form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0 28px;
}
.lp-form-col { display: flex; flex-direction: column; }
.lp-start-btn {
  width: 100%;
  margin-top: 24px;
  padding: 14px;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  border-radius: var(--radius-md);
}
.lp-form-note {
  text-align: center;
  font-size: 0.8rem;
  margin-top: 12px;
  line-height: 1.5;
}

/* ── Footer ── */
.lp-footer {
  background: var(--panel-solid);
  border-top: 1px solid var(--line);
  padding: 36px 24px;
}
.lp-footer-inner {
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.lp-footer-brand { display: flex; align-items: center; }
.lp-footer-title { font-weight: 700; font-size: 0.9rem; color: var(--ink); }
.lp-disclaimer {
  font-size: 0.8rem;
  color: var(--mut);
  line-height: 1.6;
  max-width: 700px;
  padding: 12px 16px;
  background: var(--warn-bg);
  border-left: 3px solid var(--warn);
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
  margin: 0;
}
.lp-footer-links { display: flex; gap: 16px; flex-wrap: wrap; }
.lp-footer-links a { color: var(--acc); font-size: 0.8rem; text-decoration: none; }
.lp-footer-links a:hover { text-decoration: underline; }
.lp-footer-copy { font-size: 0.75rem; color: var(--mut); margin: 0; }

/* ── RTL support ── */
[dir="rtl"] .lp-hero-inner { direction: rtl; }
[dir="rtl"] #lp-nav { direction: rtl; }
[dir="rtl"] .lp-disclaimer { border-left: none; border-right: 3px solid var(--warn); }
[dir="rtl"] .lp-challenge-info { direction: rtl; }
[dir="rtl"] .lp-flow-arrow { transform: scaleX(-1); }

/* ── Responsive ── */
@media (max-width: 860px) {
  .lp-hero-inner { grid-template-columns: 1fr; text-align: center; }
  .lp-hero-btns { justify-content: center; }
  .lp-hero-visual { display: none; }
  .lp-about-inner { grid-template-columns: 1fr; }
  .lp-about-visual { display: none; }
  .lp-form-grid { grid-template-columns: 1fr; }
  .lp-nav-links { display: none; }
}
@media (max-width: 540px) {
  .lp-section { padding: 50px 16px; }
  .lp-team-grid { grid-template-columns: repeat(2, 1fr); }
  .lp-flow { flex-direction: column; }
  .lp-flow-arrow { transform: rotate(90deg); }
  [dir="rtl"] .lp-flow-arrow { transform: rotate(90deg); }
}

/* ── Reduced motion ── */
@media (prefers-reduced-motion: reduce) {
  .lp-stars span, .lp-scroll-cue, .lp-hud-pulse,
  .lp-ecg-path, .lp-btn-primary, .lp-btn-ghost { animation: none !important; }
  .lp-prob-card:hover, .lp-feat:hover, .lp-member:hover { transform: none; }
}
'''

LANG_JS = r'''
/* ── LANDING PAGE i18n & LANG SWITCH ── */
(function(){
  const LP_LANG_KEY = 'chc-lang';
  let currentLang = 'en';
  try { currentLang = localStorage.getItem(LP_LANG_KEY) || 'en'; } catch(e){}

  function applyLang(lang){
    currentLang = lang;
    const isAr = lang === 'ar';
    document.documentElement.lang = lang;
    document.documentElement.dir = isAr ? 'rtl' : 'ltr';
    document.querySelectorAll('[data-en]').forEach(el => {
      const val = isAr ? el.dataset.ar : el.dataset.en;
      if(!val) return;
      if(el.tagName === 'INPUT' || el.tagName === 'OPTION' || el.tagName === 'SELECT') {
        if(el.tagName === 'INPUT') el.placeholder = val;
      } else {
        el.innerHTML = val;
      }
    });
    const btn = document.getElementById('lpLang');
    if(btn) btn.textContent = isAr ? 'English' : '\u0639\u0631\u0628\u064a';
    try { localStorage.setItem(LP_LANG_KEY, lang); } catch(e){}
  }

  // Apply on load
  applyLang(currentLang);

  // Bind toggle
  const langBtn = document.getElementById('lpLang');
  if(langBtn) langBtn.onclick = () => applyLang(currentLang === 'en' ? 'ar' : 'en');
})();
'''

# Read the full file
with open('Crew Health Console.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Find the CSS insertion point just before </style></head><body>
# We need to inject the landing CSS into the <style> block
style_end_marker = '</style></head><body>'
assert style_end_marker in html, "Cannot find style end marker"

html = html.replace(style_end_marker, LANDING_CSS + '\n' + style_end_marker, 1)

# 2. Find the old login block:  <div id="dim"></div><div id="login" ...>...</div></div>
# It ends just before <div id="app" hidden>
OLD_LOGIN_START = '<div id="dim"></div><div id="login"'
OLD_LOGIN_END = '</div>\n\n<div id="app" hidden>'

start_idx = html.index(OLD_LOGIN_START)
# Find where the </div></div> is before <div id="app" hidden>
app_marker = '<div id="app" hidden>'
app_idx = html.index(app_marker, start_idx)
# The old login ends with </div></div>\n\n just before app_marker
old_login_block = html[start_idx:app_idx]
html = html[:start_idx] + NEW_LOGIN + '\n\n' + html[app_idx:]

# 3. Inject the lang JS just before the closing </script> tag
script_end = '</script>'
last_script_end = html.rfind(script_end)
assert last_script_end != -1
html = html[:last_script_end] + LANG_JS + '\n' + html[last_script_end:]

# 4. Verify critical IDs still present
checks = [
    'id="login"', 'id="app"', 'id="go"', 'id="lName"', 'id="lBlood"',
    'id="lSex"', 'id="lGene"', 'id="lEnv"', 'id="lSanctuary"',
    'id="lp-hero"', 'id="lp-problem"', 'id="lp-solution"', 'id="lp-team"',
    'id="lp-signin"', 'id="lp-nav"', 'id="lpThm"', 'id="lpLang"',
    'id="fig"', 'id="tiles"', 'id="charts"', 'id="hdrSlp"', 'id="out"'
]
all_ok = True
for c in checks:
    if c not in html:
        print(f'MISSING: {c}')
        all_ok = False
if all_ok:
    print('All critical elements verified present')

print(f'Final file: {len(html)} chars, {html.count(chr(10))} lines')
print(f'Sections: {html.count("<section")} open / {html.count("</section>")} close')
print(f'Divs: {html.count("<div")} open / {html.count("</div>")} close')

with open('Crew Health Console.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Written successfully')
