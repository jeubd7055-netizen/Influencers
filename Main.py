<meta name="claude:viewport-fit-sides" content="cover">
<title>От классиков до блогеров</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Концепция: одна читаемая колонка. Классика набрана антиквой, блогеры гротеском:
   различие шрифтов само становится частью аргумента. Акцент один, ультрамарин. */
:root {
  --bg: #F3F3EF;
  --surface: #E8E9E3;
  --fg: #15171B;
  --muted: #545A64;
  --line: #C9CCC4;
  --accent: #2C47C9;
  --accent-fg: #FFFFFF;
  --pos: #1D6B4E;
  --neg: #A03A29;
  --font-display: "Newsreader", Georgia, "Times New Roman", serif;
  --font-body: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #0F1113;
    --surface: #171A1E;
    --fg: #E8E9E4;
    --muted: #9CA2AB;
    --line: #2C3138;
    --accent: #8FA3FF;
    --accent-fg: #0F1113;
    --pos: #63C89D;
    --neg: #EF8B75;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --bg: #0F1113;
  --surface: #171A1E;
  --fg: #E8E9E4;
  --muted: #9CA2AB;
  --line: #2C3138;
  --accent: #8FA3FF;
  --accent-fg: #0F1113;
  --pos: #63C89D;
  --neg: #EF8B75;
  color-scheme: dark;
}

*, *::before, *::after { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--fg);
  font: 400 1.0625rem/1.6 var(--font-body);
  -webkit-font-smoothing: antialiased;
  hyphens: auto;
}
body::before {
  content: "";
  position: fixed;
  inset: 0 0 auto 0;
  height: env(safe-area-inset-top, 0px);
  z-index: 10;
  background: var(--bg);
}
button, input { font: inherit; color: inherit; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }

h1, h2, h3, h4 { margin: 0; text-wrap: balance; }
h2 { font: 500 clamp(1.9rem, 4.2vw, 2.9rem)/1.1 var(--font-display); letter-spacing: -0.01em; }
h3 { font: 600 1.15rem/1.3 var(--font-body); }
p { margin: 0; }

.wrap {
  max-width: 1120px;
  margin-inline: auto;
  padding-left: max(16px, env(safe-area-inset-left, 0px));
  padding-right: max(16px, env(safe-area-inset-right, 0px));
}
section[id], footer[id] { scroll-margin-top: 4.5rem; }

/* Шапка */
.site-header {
  position: sticky;
  top: env(safe-area-inset-top, 0px);
  z-index: 5;
  background: var(--bg);
  border-bottom: 1px solid var(--line);
}
.site-header .wrap {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 0.6rem 1rem;
  padding-block: 0.7rem;
}
.brand {
  font: 500 0.78rem/1 var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--fg);
  text-decoration: none;
}
.nav {
  display: flex;
  gap: 1.1rem;
  min-width: 0;
  max-width: 100%;
  overflow-x: auto;
}
.nav a {
  color: var(--muted);
  text-decoration: none;
  font-size: 0.92rem;
  white-space: nowrap;
  padding-block: 0.3rem;
  border-bottom: 1px solid transparent;
}
.nav a:hover { color: var(--fg); border-bottom-color: var(--accent); }
.theme-toggle {
  min-height: 44px;
  padding: 0.4rem 0.8rem;
  font: 500 0.72rem/1 var(--font-mono);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--fg);
  background: transparent;
  border: 1px solid var(--line);
  cursor: pointer;
}
.theme-toggle:hover { border-color: var(--fg); }
@media (max-width: 639px) {
  .nav { order: 3; flex-basis: 100%; }
}

/* Общие элементы */
.eyebrow {
  font: 500 0.75rem/1.4 var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 1rem;
}
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  padding: 0.6rem 1.2rem;
  font: 500 0.95rem/1.2 var(--font-body);
  text-decoration: none;
  color: var(--accent-fg);
  background: var(--accent);
  border: 1px solid var(--accent);
  cursor: pointer;
}
.btn:hover { opacity: 0.9; }
.btn-ghost { color: var(--fg); background: transparent; border-color: var(--line); }
.btn-ghost:hover { opacity: 1; border-color: var(--fg); }

/* Hero */
.hero { padding-block: clamp(3.5rem, 9vw, 7rem) clamp(3rem, 6vw, 5rem); }
.hero h1 {
  font: 500 clamp(2.5rem, 7vw, 5.25rem)/1.02 var(--font-display);
  letter-spacing: -0.02em;
  max-width: 15ch;
}
.lede {
  font-size: clamp(1.08rem, 2vw, 1.28rem);
  line-height: 1.55;
  color: var(--muted);
  max-width: 38rem;
  margin-top: 1.5rem;
}
.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 2rem;
}
.scheme {
  margin: clamp(2.5rem, 6vw, 4.5rem) 0 0;
  padding: clamp(1.1rem, 3vw, 1.6rem);
  max-width: 46rem;
  display: grid;
  gap: 1.1rem;
  background: var(--surface);
  border: 1px solid var(--line);
}
.track {
  display: grid;
  grid-template-columns: minmax(0, 9.5rem) minmax(0, 1fr);
  gap: 1rem;
  align-items: center;
}
.track-name { display: block; font-weight: 600; }
.track-note { display: block; font-size: 0.86rem; color: var(--muted); }
.track-bar { display: block; height: 0.7rem; width: var(--w); background: var(--fg); }
.track-bar.is-blog { background: var(--accent); }
.scheme figcaption { font-size: 0.86rem; color: var(--muted); }

/* Секции */
.section { padding-block: clamp(3.5rem, 8vw, 6.5rem); }
.section.is-tinted { background: var(--surface); }
.section-head {
  max-width: 46rem;
  margin-bottom: clamp(2rem, 4vw, 3rem);
}
.section-head p:not(.eyebrow) { margin-top: 1rem; color: var(--muted); }

/* Сравнение: вкладки */
.tablist {
  display: flex;
  flex-wrap: wrap;
  gap: 0 1.6rem;
  border-bottom: 1px solid var(--line);
  margin-bottom: 2rem;
}
.tab {
  appearance: none;
  background: none;
  border: 0;
  border-bottom: 2px solid transparent;
  margin-bottom: -1px;
  padding: 0.75rem 0;
  min-height: 44px;
  font: 500 1rem/1.2 var(--font-body);
  color: var(--muted);
  cursor: pointer;
}
.tab:hover { color: var(--fg); }
.tab[aria-selected="true"] { color: var(--fg); border-bottom-color: var(--accent); }
.compare { display: grid; gap: 1rem; }
@media (min-width: 760px) {
  .compare { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 1.25rem; }
}
.side {
  min-width: 0;
  padding: clamp(1.25rem, 3vw, 2rem);
  background: var(--bg);
  border: 1px solid var(--line);
}
.side-blog { background: var(--surface); }
.side-tag {
  font: 500 0.72rem/1.4 var(--font-mono);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}
.side h3 { margin-top: 0.6rem; }
.side-classic h3 { font: 500 1.7rem/1.2 var(--font-display); }
.side-blog h3 { font: 600 1.2rem/1.3 var(--font-body); }
.side p:not(.side-tag) { margin-top: 0.8rem; line-height: 1.6; }
.verdict {
  margin-top: 1.25rem;
  max-width: 46rem;
}
.verdict strong { font-weight: 600; color: var(--accent); }

/* Анализ */
.split { display: grid; gap: 3rem; }
@media (min-width: 820px) {
  .split { grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 3.5rem; }
}
.split > * { min-width: 0; }
.split h3 {
  display: flex;
  align-items: baseline;
  gap: 0.6rem;
  font: 500 1.45rem/1.2 var(--font-display);
  padding-bottom: 0.8rem;
  border-bottom: 2px solid var(--fg);
}
.mark { font: 500 1.3rem/1 var(--font-mono); }
.mark-pos { color: var(--pos); }
.mark-neg { color: var(--neg); }
.items { list-style: none; margin: 0; padding: 0; }
.items li {
  padding-block: 1.1rem;
  border-bottom: 1px solid var(--line);
}
.items h4 { font: 600 1.02rem/1.35 var(--font-body); margin-bottom: 0.35rem; }
.items p { color: var(--muted); font-size: 0.98rem; }
.balance {
  margin-top: clamp(2.5rem, 5vw, 3.5rem);
  padding: clamp(1.25rem, 3vw, 1.75rem);
  max-width: 50rem;
  background: var(--bg);
  border: 1px solid var(--line);
}
.balance p { font: 500 clamp(1.1rem, 2.4vw, 1.3rem)/1.5 var(--font-display); }

/* Квиз */
.quiz {
  max-width: 46rem;
  padding: clamp(1.25rem, 4vw, 2.25rem);
  background: var(--bg);
  border: 1px solid var(--line);
}
.progress { height: 3px; background: var(--line); }
.progress-fill {
  display: block;
  height: 100%;
  width: 0;
  background: var(--accent);
  transition: width 0.3s ease;
}
.quiz-meta {
  margin-top: 1rem;
  font: 500 0.75rem/1.4 var(--font-mono);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
}
.quiz-title {
  margin-top: 1.25rem;
  font: 500 clamp(1.4rem, 3vw, 1.75rem)/1.25 var(--font-display);
}
.quiz-text { margin-top: 0.9rem; line-height: 1.6; }
.quiz-options {
  display: grid;
  gap: 0.6rem;
  margin-top: 1.6rem;
}
@media (min-width: 600px) {
  .quiz-options { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
.opt {
  min-height: 48px;
  padding: 0.7rem 0.9rem;
  font: 500 0.95rem/1.3 var(--font-body);
  text-align: left;
  color: var(--fg);
  background: transparent;
  border: 1px solid var(--line);
  cursor: pointer;
}
.opt:hover:not(:disabled) { border-color: var(--fg); }
.opt:disabled { cursor: default; }
.opt.is-correct { border-color: var(--pos); box-shadow: inset 0 0 0 1px var(--pos); color: var(--pos); }
.opt.is-wrong { border-color: var(--neg); box-shadow: inset 0 0 0 1px var(--neg); color: var(--neg); }
.feedback {
  margin-top: 1.6rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--line);
}
.feedback-verdict { font-weight: 600; }
.feedback-text { margin-top: 0.5rem; color: var(--muted); }
.quiz-next { margin-top: 1.25rem; }
.score {
  font: 500 3.2rem/1 var(--font-display);
  margin-top: 0.5rem;
}
.result-text { margin-top: 1rem; }
.result .quiz-next { margin-top: 1.5rem; }

/* Подвал: выводы */
.site-footer {
  background: var(--surface);
  border-top: 1px solid var(--line);
  padding-block: clamp(3.5rem, 8vw, 6rem) 2rem;
}
.conclusions { display: grid; gap: 3rem; }
@media (min-width: 880px) {
  .conclusions { grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.85fr); gap: 4.5rem; }
}
.conclusions > * { min-width: 0; }
.footer-lede { margin-top: 1rem; color: var(--muted); max-width: 40rem; }
.concl { list-style: none; margin: 2rem 0 0; padding: 0; }
.concl li {
  padding-block: 1.1rem;
  border-top: 1px solid var(--line);
}
.concl strong { display: block; font-weight: 600; margin-bottom: 0.3rem; }
.checklist {
  min-width: 0;
  margin: 0;
  padding: clamp(1.25rem, 3vw, 1.75rem);
  background: var(--bg);
  border: 1px solid var(--line);
}
.checklist legend { padding: 0 0 0.75rem; }
.check {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  min-height: 44px;
  padding-block: 0.45rem;
  cursor: pointer;
}
.check input {
  flex: 0 0 auto;
  width: 1.1rem;
  height: 1.1rem;
  margin-top: 0.2rem;
  accent-color: var(--accent);
}
.check span { flex: 1 1 auto; min-width: 0; }
.colophon {
  margin-top: clamp(3rem, 6vw, 4.5rem);
  padding-top: 1.5rem;
  border-top: 1px solid var(--line);
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 1rem;
  font-size: 0.9rem;
  color: var(--muted);
}
.colophon p { max-width: 40rem; }

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .progress-fill { transition: none; }
}
</style>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="#top">Медиа и мысль</a>
    <nav class="nav" aria-label="Разделы страницы">
      <a href="#compare">Сравнение</a>
      <a href="#analysis">Аспекты</a>
      <a href="#quiz">Проверка</a>
      <a href="#conclusions">Выводы</a>
    </nav>
    <button class="theme-toggle" id="theme-toggle" type="button">Тёмная тема</button>
  </div>
</header>

<main id="main">

  <section class="hero" id="top">
    <div class="wrap">
      <p class="eyebrow">Медиа · Воспитание · Мышление</p>
      <h1>Учитель из книги или из ленты?</h1>
      <p class="lede">Философы прошлого формировали мышление годами: через трактаты, письма и споры. Блогеры делают похожую работу за считанные минуты, на экране телефона. Разбираем, что это меняет в сознании и воспитании молодёжи и как трезво оценивать такое влияние.</p>
      <div class="hero-actions">
        <a class="btn" href="#compare">Сравнить подходы</a>
        <a class="btn btn-ghost" href="#quiz">Проверить себя</a>
      </div>
      <figure class="scheme">
        <div class="track">
          <div>
            <span class="track-name">Классики</span>
            <span class="track-note">Идеи живут поколениями</span>
          </div>
          <span class="track-bar" style="--w: 100%"></span>
        </div>
        <div class="track">
          <div>
            <span class="track-name">Лента</span>
            <span class="track-note">Тренд живёт неделями</span>
          </div>
          <span class="track-bar is-blog" style="--w: 30%"></span>
        </div>
        <figcaption>Схема показывает относительную длительность влияния. Это иллюстрация, а не измерение.</figcaption>
      </figure>
    </div>
  </section>

  <section class="section" id="compare" aria-labelledby="compare-title">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Сравнение</p>
        <h2 id="compare-title">Два способа повлиять на мысль</h2>
        <p>Выберите параметр. Слева классические авторы: трактаты, диалоги, эссе. Справа современные блогеры в YouTube и Telegram. Сравниваем форму влияния, а не конкретных людей.</p>
      </div>

      <div class="tablist" role="tablist" aria-label="Параметры сравнения">
        <button class="tab" role="tab" id="tab-format" aria-controls="panel-format" aria-selected="true" tabindex="0" type="button">Формат</button>
        <button class="tab" role="tab" id="tab-speed" aria-controls="panel-speed" aria-selected="false" tabindex="-1" type="button">Скорость</button>
        <button class="tab" role="tab" id="tab-depth" aria-controls="panel-depth" aria-selected="false" tabindex="-1" type="button">Глубина</button>
        <button class="tab" role="tab" id="tab-authority" aria-controls="panel-authority" aria-selected="false" tabindex="-1" type="button">Авторитет</button>
      </div>

      <div class="panel" role="tabpanel" id="panel-format" aria-labelledby="tab-format">
        <div class="compare">
          <article class="side side-classic">
            <p class="side-tag">Классики</p>
            <h3>Трактат и диалог</h3>
            <p>Длинный текст, который требует внимания от начала до конца. Аргумент строится шаг за шагом, и читатель проходит путь вместе с автором.</p>
          </article>
          <article class="side side-blog">
            <p class="side-tag">Блогеры</p>
            <h3>Короткое видео и пост</h3>
            <p>Вертикальный ролик, карусель или серия сторис, рассчитанные на один просмотр. Мысль подаётся готовым выводом, поэтому её легко запомнить и трудно проверить.</p>
          </article>
        </div>
        <p class="verdict"><strong>Вывод.</strong> Формат блогера экономит внимание и открывает вход в тему. Формат классика учит удерживать мысль дольше одной минуты.</p>
      </div>

      <div class="panel" role="tabpanel" id="panel-speed" aria-labelledby="tab-speed" hidden>
        <div class="compare">
          <article class="side side-classic">
            <p class="side-tag">Классики</p>
            <h3>Поколения</h3>
            <p>Идея проходит через десятилетия. Книгу переиздают, цитируют и спорят с ней. Влияние накапливается медленно и почти незаметно.</p>
          </article>
          <article class="side side-blog">
            <p class="side-tag">Блогеры</p>
            <h3>Часы и недели</h3>
            <p>Охват появляется за сутки, а иногда и быстрее. Тренд сменяется так же быстро, и вместе с ним уходят и ценности, и авторитет.</p>
          </article>
        </div>
        <p class="verdict"><strong>Вывод.</strong> Быстрота даёт интерес и присутствие, медлительность даёт опору. Для устойчивых взглядов нужны обе скорости.</p>
      </div>

      <div class="panel" role="tabpanel" id="panel-depth" aria-labelledby="tab-depth" hidden>
        <div class="compare">
          <article class="side side-classic">
            <p class="side-tag">Классики</p>
            <h3>Контекст и спор</h3>
            <p>Автор работает с противоречиями, оговаривает границы своих выводов и нередко оставляет вопрос открытым. Читатель видит не только вывод, но и путь к нему.</p>
          </article>
          <article class="side side-blog">
            <p class="side-tag">Блогеры</p>
            <h3>Одна идея за выпуск</h3>
            <p>Сложная тема сжимается до тезиса, который держится на примере и эмоции. Упрощение бывает честным, но часто стирает оговорки, без которых тезис верен лишь отчасти.</p>
          </article>
        </div>
        <p class="verdict"><strong>Вывод.</strong> Глубина классика требует усилия. Глубина блогера зависит от того, называет ли он источники и показывает ли границы своего тезиса.</p>
      </div>

      <div class="panel" role="tabpanel" id="panel-authority" aria-labelledby="tab-authority" hidden>
        <div class="compare">
          <article class="side side-classic">
            <p class="side-tag">Классики</p>
            <h3>Традиция и критика</h3>
            <p>Вес текста держится на веках чтения, филологическом разборе и спорах современников. Его можно проверить, сопоставив с другими источниками.</p>
          </article>
          <article class="side side-blog">
            <p class="side-tag">Блогеры</p>
            <h3>Личная близость</h3>
            <p>Доверие строится на ощущении, что автор говорит именно с тобой: в кадре, в комментариях, в личных историях. Механизм сильный, и проверки он обычно не требует.</p>
          </article>
        </div>
        <p class="verdict"><strong>Вывод.</strong> Классика просит доверять тексту, блогер просит доверять человеку. Ошибку человека, который нравится, заметить труднее.</p>
      </div>
    </div>
  </section>

  <section class="section is-tinted" id="analysis" aria-labelledby="analysis-title">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Анализ</p>
        <h2 id="analysis-title">Что даёт влияние, а что отнимает</h2>
        <p>Одно и то же содержание может поднять интерес к теме или сломать его. Ниже перечислены повторяющиеся эффекты, которые проявляются у молодой аудитории в обоих форматах.</p>
      </div>

      <div class="split">
        <div>
          <h3><span class="mark mark-pos" aria-hidden="true">+</span>Что даёт</h3>
          <ul class="items">
            <li>
              <h4>Доступ к идеям</h4>
              <p>Сложные темы объясняются языком, который не требует подготовки. Это может стать первым шагом к чтению.</p>
            </li>
            <li>
              <h4>Вопрос вместо ответа</h4>
              <p>Хорошая подача вызывает желание проверить и поспорить, а не просто согласиться.</p>
            </li>
            <li>
              <h4>Разнообразие голосов</h4>
              <p>Лента быстро показывает разные точки зрения, в том числе те, что редко звучат в школе или в семье.</p>
            </li>
            <li>
              <h4>Ощущение, что тебя услышали</h4>
              <p>Молодой человек видит, что его тревоги и вопросы кто-то разбирает всерьёз.</p>
            </li>
          </ul>
        </div>

        <div>
          <h3><span class="mark mark-neg" aria-hidden="true">−</span>Что отнимает</h3>
          <ul class="items">
            <li>
              <h4>Подмена глубины</h4>
              <p>Тезис за минуту вытесняет ход рассуждения, в котором есть сомнение и контекст.</p>
            </li>
            <li>
              <h4>Награда за громкость</h4>
              <p>Платформы выигрывают от резких суждений, поэтому точные и осторожные голоса теряют охват.</p>
            </li>
            <li>
              <h4>Образец для подражания</h4>
              <p>Человек, которого смотрят каждый день, становится ориентиром во вкусе, решениях и самооценке.</p>
            </li>
            <li>
              <h4>Давление ср
