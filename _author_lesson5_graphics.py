"""Add SVG graphics to Lesson 5 (loops) of the Java OCA course."""
from app import app, Lesson, db

COURSE_TITLE_FRAG = '1Z0-808'
LESSON_TITLE = 'Lesson 5: Using Loop Constructs'

LESSON_HTML = """
<style>
  .lsn-h2{font-size:1.5rem;font-weight:600;margin:32px 0 12px;letter-spacing:-0.005em;}
  .lsn-p{font-size:1.0625rem;line-height:1.7;margin:0 0 14px;}
  .lsn-ul{font-size:1.0625rem;line-height:1.7;margin:0 0 18px 1.25rem;padding:0;}
  .lsn-callout{background:rgba(127,127,127,.10);padding:14px 18px;border-radius:6px;margin:18px 0;}
  .lsn-warn{background:rgba(127,127,127,.14);padding:14px 18px;border-radius:6px;margin:18px 0;}
  .lsn-table{width:100%;border-collapse:collapse;margin:14px 0 22px;font-size:1rem;}
  .lsn-table th,.lsn-table td{border:1px solid rgba(127,127,127,.35);padding:10px 12px;text-align:left;vertical-align:top;}
  .lsn-table th{background:rgba(127,127,127,.10);font-weight:600;}
  .lsn-fig{margin:22px auto;max-width:560px;text-align:center;}
  .lsn-fig svg{max-width:100%;height:auto;display:block;margin:0 auto;}
  .lsn-cap{font-size:.9rem;color:#6B6B6B;margin-top:6px;}
</style>

<p class="lsn-p">Loops let you execute the same block of code many times. Java offers four loop forms &mdash; <code>while</code>, <code>do/while</code>, the classic <code>for</code> and the enhanced <code>for</code> (&ldquo;for-each&rdquo;) &mdash; together with the <code>break</code> and <code>continue</code> control-flow keywords. Choosing the right loop is mostly about <em>when</em> the condition is tested and <em>what</em> you need to iterate over.</p>

<div class="lsn-callout"><strong>Learning objectives.</strong> By the end of this lesson you should be able to: create and use <code>while</code>, <code>do/while</code>, classic <code>for</code> and enhanced <code>for</code> loops; compare the four loop constructs; and use <code>break</code> and <code>continue</code> (including labelled forms) to alter loop flow.</div>

<h2 class="lsn-h2">1. The <code>while</code> loop</h2>
<p class="lsn-p">A <code>while</code> loop tests its <code>boolean</code> condition <em>before</em> each iteration, so the body may execute zero times:</p>
<pre><code>int i = 0;
while (i &lt; 3) {
    System.out.println(i);
    i++;
}
// prints 0, 1, 2
</code></pre>

<figure class="lsn-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 240" role="img" aria-label="while loop flowchart">
    <defs>
      <marker id="arrW" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="#6B6B6B"/>
      </marker>
    </defs>
    <g fill="rgba(127,127,127,.10)" stroke="#6B6B6B" stroke-width="1.5">
      <ellipse cx="180" cy="22" rx="44" ry="16"/>
      <polygon points="180,60 240,90 180,120 120,90"/>
      <rect x="130" y="170" width="100" height="40" rx="4"/>
      <ellipse cx="44" cy="90" rx="36" ry="16"/>
    </g>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <line x1="180" y1="38" x2="180" y2="58" marker-end="url(#arrW)"/>
      <line x1="180" y1="120" x2="180" y2="168" marker-end="url(#arrW)"/>
      <polyline points="230,190 300,190 300,90 242,90" marker-end="url(#arrW)"/>
      <line x1="120" y1="90" x2="82" y2="90" marker-end="url(#arrW)"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="13" text-anchor="middle">
      <text x="180" y="27">start</text>
      <text x="180" y="94">cond?</text>
      <text x="180" y="195">body</text>
      <text x="44" y="95">end</text>
    </g>
    <g fill="#6B6B6B" font-family="system-ui,sans-serif" font-size="12">
      <text x="186" y="148">true</text>
      <text x="86" y="82">false</text>
    </g>
  </svg>
  <div class="lsn-cap">Figure 1. <code>while</code> &mdash; the condition is tested <em>before</em> the body, so the body may run zero times.</div>
</figure>

<h2 class="lsn-h2">2. The <code>do/while</code> loop</h2>
<p class="lsn-p">A <code>do/while</code> loop tests its condition <em>after</em> each iteration, so the body always executes at least once. Note the mandatory trailing semicolon:</p>
<pre><code>int n = 10;
do {
    System.out.println(n);
    n++;
} while (n &lt; 3);
// prints 10 (once), then stops
</code></pre>

<figure class="lsn-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 220" role="img" aria-label="do-while loop flowchart">
    <defs>
      <marker id="arrDW" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="#6B6B6B"/>
      </marker>
    </defs>
    <g fill="rgba(127,127,127,.10)" stroke="#6B6B6B" stroke-width="1.5">
      <ellipse cx="180" cy="22" rx="44" ry="16"/>
      <rect x="130" y="60" width="100" height="40" rx="4"/>
      <polygon points="180,130 240,160 180,190 120,160"/>
      <ellipse cx="44" cy="160" rx="36" ry="16"/>
    </g>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <line x1="180" y1="38" x2="180" y2="58" marker-end="url(#arrDW)"/>
      <line x1="180" y1="100" x2="180" y2="128" marker-end="url(#arrDW)"/>
      <polyline points="240,160 300,160 300,80 232,80" marker-end="url(#arrDW)"/>
      <line x1="120" y1="160" x2="82" y2="160" marker-end="url(#arrDW)"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="13" text-anchor="middle">
      <text x="180" y="85">body</text>
      <text x="180" y="164">cond?</text>
      <text x="180" y="27">start</text>
      <text x="44" y="165">end</text>
    </g>
    <g fill="#6B6B6B" font-family="system-ui,sans-serif" font-size="12">
      <text x="306" y="125">true</text>
      <text x="86" y="152">false</text>
    </g>
  </svg>
  <div class="lsn-cap">Figure 2. <code>do/while</code> &mdash; the body runs first, then the condition is tested, so the body always runs at least once.</div>
</figure>

<h2 class="lsn-h2">3. The classic <code>for</code> loop</h2>
<p class="lsn-p">The classic <code>for</code> packs initialization, condition and update onto one line. All three sections are optional &mdash; an empty condition is treated as <code>true</code>, producing an infinite loop:</p>
<pre><code>for (int i = 0; i &lt; 5; i++) {
    System.out.print(i + " ");
}
// 0 1 2 3 4

for (;;) {                 // infinite loop &mdash; legal
    if (Math.random() &gt; 0.99) break;
}
</code></pre>

<div class="lsn-callout">You may declare <strong>multiple variables of the same type</strong> in the initializer, and use a comma list for the update; you cannot mix types or use commas in the condition.</div>
<pre><code>for (int a = 0, b = 10; a &lt; b; a++, b--) {
    System.out.println(a + " " + b);
}
</code></pre>

<figure class="lsn-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 260" role="img" aria-label="classic for loop flowchart">
    <defs>
      <marker id="arrF" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="#6B6B6B"/>
      </marker>
    </defs>
    <g fill="rgba(127,127,127,.10)" stroke="#6B6B6B" stroke-width="1.5">
      <ellipse cx="220" cy="22" rx="44" ry="16"/>
      <rect x="160" y="60" width="120" height="36" rx="4"/>
      <polygon points="220,110 290,140 220,170 150,140"/>
      <rect x="170" y="200" width="100" height="38" rx="4"/>
      <rect x="320" y="200" width="100" height="38" rx="4"/>
      <ellipse cx="60" cy="140" rx="36" ry="16"/>
    </g>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <line x1="220" y1="38" x2="220" y2="58" marker-end="url(#arrF)"/>
      <line x1="220" y1="96" x2="220" y2="108" marker-end="url(#arrF)"/>
      <line x1="220" y1="170" x2="220" y2="198" marker-end="url(#arrF)"/>
      <line x1="270" y1="219" x2="318" y2="219" marker-end="url(#arrF)"/>
      <polyline points="370,200 370,140 292,140" marker-end="url(#arrF)"/>
      <line x1="150" y1="140" x2="98" y2="140" marker-end="url(#arrF)"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="13" text-anchor="middle">
      <text x="220" y="27">start</text>
      <text x="220" y="84">init</text>
      <text x="220" y="144">cond?</text>
      <text x="220" y="224">body</text>
      <text x="370" y="224">update</text>
      <text x="60" y="145">end</text>
    </g>
    <g fill="#6B6B6B" font-family="system-ui,sans-serif" font-size="12">
      <text x="226" y="190">true</text>
      <text x="104" y="132">false</text>
    </g>
  </svg>
  <div class="lsn-cap">Figure 3. Classic <code>for</code> &mdash; <em>init</em> runs once; then <em>cond</em>, <em>body</em>, <em>update</em> cycle until <em>cond</em> is false.</div>
</figure>

<h2 class="lsn-h2">4. The enhanced <code>for</code> (&ldquo;for-each&rdquo;)</h2>
<p class="lsn-p">The enhanced <code>for</code> reads each element of an array or anything that implements <code>Iterable</code>. You give up the index in exchange for cleaner code:</p>
<pre><code>String[] names = {"Ada", "Linus", "Grace"};
for (String name : names) {
    System.out.println(name);
}
</code></pre>

<figure class="lsn-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 180" role="img" aria-label="enhanced for loop walking each element of an array">
    <defs>
      <marker id="arrE" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="#6B6B6B"/>
      </marker>
    </defs>
    <g fill="rgba(127,127,127,.10)" stroke="#6B6B6B" stroke-width="1.5">
      <rect x="40"  y="80" width="64" height="50" rx="4"/>
      <rect x="110" y="80" width="64" height="50" rx="4"/>
      <rect x="180" y="80" width="64" height="50" rx="4"/>
      <rect x="250" y="80" width="64" height="50" rx="4"/>
      <rect x="320" y="80" width="64" height="50" rx="4"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="14" text-anchor="middle">
      <text x="72"  y="111">10</text>
      <text x="142" y="111">20</text>
      <text x="212" y="111">30</text>
      <text x="282" y="111">40</text>
      <text x="352" y="111">50</text>
    </g>
    <g fill="#6B6B6B" font-family="system-ui,sans-serif" font-size="11" text-anchor="middle">
      <text x="72"  y="148">a[0]</text>
      <text x="142" y="148">a[1]</text>
      <text x="212" y="148">a[2]</text>
      <text x="282" y="148">a[3]</text>
      <text x="352" y="148">a[4]</text>
    </g>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <path d="M40,60 C 110,30 320,30 384,60" marker-end="url(#arrE)"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="13" text-anchor="middle">
      <text x="212" y="22">for (int n : a) &mdash; n takes each value in order</text>
    </g>
  </svg>
  <div class="lsn-cap">Figure 4. Enhanced <code>for</code> &mdash; visits every element left-to-right. You see the value, never the index.</div>
</figure>

<div class="lsn-warn"><strong>Common trap.</strong> Reassigning the loop variable inside an enhanced <code>for</code> does <em>not</em> change the underlying element. For primitives you hold a copy of the value; for objects you hold a copy of the reference.</div>

<h2 class="lsn-h2">5. Comparing the four loop constructs</h2>
<table class="lsn-table">
  <thead><tr><th>Loop</th><th>When the condition is tested</th><th>Best for</th></tr></thead>
  <tbody>
    <tr><td><code>while</code></td><td>Before each iteration</td><td>Repeat while some external condition holds; body may run zero times.</td></tr>
    <tr><td><code>do/while</code></td><td>After each iteration</td><td>Always run the body at least once (menu prompts, input validation).</td></tr>
    <tr><td>Classic <code>for</code></td><td>Before each iteration</td><td>Counted iteration where you need the index.</td></tr>
    <tr><td>Enhanced <code>for</code></td><td>Before each iteration</td><td>Walking every element of an array or <code>Iterable</code> when you do not need the index.</td></tr>
  </tbody>
</table>

<h2 class="lsn-h2">6. <code>break</code> and <code>continue</code></h2>
<p class="lsn-p"><code>break</code> exits the nearest enclosing loop (or <code>switch</code>). <code>continue</code> skips the rest of the current iteration and jumps to the next test (and to the update section, for a classic <code>for</code>):</p>
<pre><code>for (int i = 0; i &lt; 10; i++) {
    if (i == 3) continue;       // skip 3
    if (i == 7) break;          // stop at 7
    System.out.print(i + " ");
}
// prints: 0 1 2 4 5 6
</code></pre>

<figure class="lsn-fig">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 220" role="img" aria-label="break and continue inside a for loop">
    <defs>
      <marker id="arrBC" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
        <path d="M0,0 L10,5 L0,10 z" fill="#6B6B6B"/>
      </marker>
    </defs>
    <g fill="rgba(127,127,127,.10)" stroke="#6B6B6B" stroke-width="1.5">
      <circle cx="50"  cy="120" r="22"/>
      <circle cx="120" cy="120" r="22"/>
      <circle cx="190" cy="120" r="22"/>
      <circle cx="260" cy="120" r="22"/>
      <circle cx="330" cy="120" r="22"/>
      <circle cx="400" cy="120" r="22"/>
    </g>
    <g fill="currentColor" font-family="system-ui,sans-serif" font-size="14" text-anchor="middle">
      <text x="50"  y="125">0</text>
      <text x="120" y="125">1</text>
      <text x="190" y="125">2</text>
      <text x="260" y="125">3</text>
      <text x="330" y="125">4</text>
      <text x="400" y="125">5</text>
    </g>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <line x1="72"  y1="120" x2="96"  y2="120" marker-end="url(#arrBC)"/>
      <line x1="142" y1="120" x2="166" y2="120" marker-end="url(#arrBC)"/>
      <line x1="212" y1="120" x2="236" y2="120" marker-end="url(#arrBC)"/>
      <line x1="282" y1="120" x2="306" y2="120" marker-end="url(#arrBC)"/>
    </g>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none" stroke-dasharray="4 3">
      <path d="M190,98 C 190,55 260,55 260,98" marker-end="url(#arrBC)"/>
    </g>
    <text x="225" y="42" fill="currentColor" font-family="system-ui,sans-serif" font-size="12" text-anchor="middle">continue (skip body, go to next iteration)</text>
    <g stroke="#6B6B6B" stroke-width="1.5" fill="none">
      <line x1="352" y1="120" x2="438" y2="120" marker-end="url(#arrBC)"/>
    </g>
    <text x="396" y="108" fill="currentColor" font-family="system-ui,sans-serif" font-size="12" text-anchor="middle">break</text>
    <text x="396" y="182" fill="#6B6B6B" font-family="system-ui,sans-serif" font-size="11" text-anchor="middle">exits the loop</text>
    <text x="225" y="182" fill="#6B6B6B" font-family="system-ui,sans-serif" font-size="11" text-anchor="middle">iteration index <tspan font-style="italic">i</tspan></text>
  </svg>
  <div class="lsn-cap">Figure 5. <code>continue</code> jumps straight to the next iteration; <code>break</code> exits the loop entirely.</div>
</figure>

<h2 class="lsn-h2">7. Labelled <code>break</code> and <code>continue</code></h2>
<p class="lsn-p">With nested loops, an unlabelled <code>break</code>/<code>continue</code> only affects the innermost loop. A label lets you target an outer loop:</p>
<pre><code>outer:
for (int r = 0; r &lt; 3; r++) {
    for (int c = 0; c &lt; 3; c++) {
        if (r == 1 &amp;&amp; c == 1) break outer;   // exits BOTH loops
        System.out.println(r + "," + c);
    }
}
</code></pre>

<h2 class="lsn-h2">8. Common pitfalls</h2>
<ul class="lsn-ul">
  <li>Forgetting the semicolon after <code>do { ... } while (cond);</code> &mdash; compile error.</li>
  <li>Off-by-one errors: <code>i &lt;= a.length</code> is one step too far; use <code>i &lt; a.length</code>.</li>
  <li>Modifying the array size inside an enhanced <code>for</code> over a <code>Collection</code> throws <code>ConcurrentModificationException</code>.</li>
  <li>An empty <code>for(;;)</code> is an infinite loop &mdash; you must <code>break</code> out.</li>
  <li>A condition that is a compile-time constant <code>false</code> (e.g. <code>while(false)</code>) is a compile-time error; the body would be unreachable.</li>
</ul>

<h2 class="lsn-h2">9. Summary</h2>
<ul class="lsn-ul">
  <li><code>while</code> and the two <code>for</code> forms test <strong>before</strong> the body; <code>do/while</code> tests <strong>after</strong>.</li>
  <li>The classic <code>for</code> can declare multiple variables of one type and run multiple update expressions.</li>
  <li>The enhanced <code>for</code> hides the index; reassigning the loop variable has no effect on the source.</li>
  <li><code>break</code> exits a loop; <code>continue</code> skips to the next iteration. Labels let either keyword target an outer loop.</li>
</ul>
"""


def main():
    with app.app_context():
        lesson = Lesson.query.join(Lesson.course).filter(
            Lesson.title == LESSON_TITLE,
        ).first()
        if not lesson:
            print('Lesson 5 not found.')
            return
        lesson.content = LESSON_HTML
        db.session.commit()
        print(f'updated lesson {lesson.id} ({len(LESSON_HTML)} chars)')


if __name__ == '__main__':
    main()
