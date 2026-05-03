import { HubFeatureCard, HubHero, HubPageShell, HubSectionIntro } from '@/components/HubPage';

type HeroStat = {
  label: string;
  value: string;
  description: string;
};

type SpotlightCard = {
  eyebrow: string;
  title: string;
  description: string;
  href: string;
  cta: string;
  accent: string;
  hoverAccent: string;
};

type PhaseLink = {
  label: string;
  href: string;
};

type PhaseCard = {
  phase: string;
  title: string;
  description: string;
  accent: string;
  links: PhaseLink[];
};

type UtilityCard = {
  title: string;
  description: string;
  href: string;
};

const heroStats: HeroStat[] = [
  {
    label: 'Core path',
    value: '35+',
    description: 'Top-level modules spanning fundamentals to production AI systems.',
  },
  {
    label: 'Practice',
    value: 'Notebooks + quizzes',
    description: 'Learn with executable examples, challenge pages, and end-of-section checks.',
  },
  {
    label: 'Reference',
    value: 'Cheatsheets',
    description: 'Keep the docs open while building with quick command and architecture references.',
  },
];

const spotlightCards: SpotlightCard[] = [
  {
    eyebrow: 'New here',
    title: 'Start from zero',
    description:
      'Set up your environment, learn the repo structure, and enter the core sequence in the intended order.',
    href: '/00-course-setup',
    cta: 'Go to course setup',
    accent: 'text-sky-600 dark:text-sky-400',
    hoverAccent: 'group-hover:text-sky-700 dark:group-hover:text-sky-300',
  },
  {
    eyebrow: 'Hot path',
    title: 'Build AI agents',
    description:
      'Jump into function calling, ReAct, MCP, reasoning models, and agent evaluation if you already know the basics.',
    href: '/15-ai-agents',
    cta: 'Explore the agents track',
    accent: 'text-emerald-600 dark:text-emerald-400',
    hoverAccent: 'group-hover:text-emerald-700 dark:group-hover:text-emerald-300',
  },
  {
    eyebrow: 'Fast reference',
    title: 'Use the cheatsheets',
    description:
      'Keep Python, cloud, Kubernetes, GitHub Actions, Docker, and MLOps references close while you build.',
    href: '/32-cheatsheets',
    cta: 'Open the reference hub',
    accent: 'text-amber-600 dark:text-amber-400',
    hoverAccent: 'group-hover:text-amber-700 dark:group-hover:text-amber-300',
  },
];

const phaseCards: PhaseCard[] = [
  {
    phase: 'Phase 1',
    title: 'Foundations',
    description:
      'Build the baseline: setup, Python, data science, and math needed for everything else.',
    accent: 'hover:ring-sky-300',
    links: [
      { label: 'Course setup', href: '/00-course-setup' },
      { label: 'Python', href: '/01-python' },
      { label: 'Data science', href: '/02-data-science' },
      { label: 'Maths', href: '/03-maths' },
    ],
  },
  {
    phase: 'Phase 2',
    title: 'LLM and agent systems',
    description:
      'Move from tokens and embeddings into RAG, fine-tuning, multimodal systems, local models, and agents.',
    accent: 'hover:ring-emerald-300',
    links: [
      { label: 'Tokenization', href: '/04-token' },
      { label: 'Embeddings', href: '/05-embeddings' },
      { label: 'RAG', href: '/08-rag' },
      { label: 'Fine-tuning', href: '/12-llm-finetuning' },
      { label: 'AI agents', href: '/15-ai-agents' },
    ],
  },
  {
    phase: 'Phase 3',
    title: 'Production and specialization',
    description:
      'Add evaluation, safety, real-time systems, advanced deep learning, reinforcement learning, and practical specializations.',
    accent: 'hover:ring-amber-300',
    links: [
      { label: 'MLOps', href: '/09-mlops' },
      { label: 'Evaluation', href: '/16-model-evaluation' },
      { label: 'Safety', href: '/19-ai-safety-redteaming' },
      { label: 'Advanced DL', href: '/24-advanced-deep-learning' },
      { label: 'Practical DS', href: '/28-practical-data-science' },
    ],
  },
];

const utilityCards: UtilityCard[] = [
  {
    title: 'Quizzes',
    description: 'Pressure-test understanding before you move deeper into the curriculum.',
    href: '/21-quizzes',
  },
  {
    title: 'Cheatsheets',
    description: 'Keep command references and architecture notes open while you work.',
    href: '/32-cheatsheets',
  },
  {
    title: 'References',
    description: 'Use curated references when you need source material, not just tutorials.',
    href: '/22-references',
  },
  {
    title: 'Glossary',
    description: 'Bridge the gap between reading fast and understanding the vocabulary.',
    href: '/23-glossary',
  },
];

const quickLinks: PhaseLink[] = [
  { label: 'AI-powered dev tools', href: '/31-ai-powered-dev-tools' },
  { label: 'Real-time streaming systems', href: '/20-real-time-streaming' },
  { label: 'Inference optimization', href: '/30-inference-optimization' },
  { label: 'AI hardware and LLM validation', href: '/29-ai-hardware-llm-validation' },
  { label: 'Interactive app demos', href: '/app' },
];

function Phase({ card }: { card: PhaseCard }) {
  return (
    <div className="rounded-3xl border border-slate-200 bg-slate-50 p-6 dark:border-slate-800 dark:bg-slate-900/50">
      <p className="text-sm font-semibold uppercase tracking-[0.18em] text-slate-500 dark:text-slate-400">{card.phase}</p>
      <h3 className="mt-2 text-2xl font-bold text-slate-900 dark:text-white">{card.title}</h3>
      <p className="mt-3 text-sm leading-7 text-slate-600 dark:text-slate-300">{card.description}</p>
      <div className="mt-5 flex flex-wrap gap-3 text-sm">
        {card.links.map((link) => (
          <a
            key={link.href}
            href={link.href}
            className={`rounded-full bg-white px-4 py-2 font-medium text-slate-800 ring-1 ring-slate-200 transition dark:bg-slate-950 dark:text-slate-100 dark:ring-slate-700 ${card.accent}`}
          >
            {link.label}
          </a>
        ))}
      </div>
    </div>
  );
}

function Utility({ card }: { card: UtilityCard }) {
  return (
    <a
      href={card.href}
      className="rounded-2xl border border-slate-200 p-5 transition hover:border-sky-300 hover:bg-sky-50/60 dark:border-slate-800 dark:hover:border-sky-800 dark:hover:bg-slate-800/60"
    >
      <h3 className="text-lg font-semibold text-slate-900 dark:text-white">{card.title}</h3>
      <p className="mt-2 text-sm leading-7 text-slate-600 dark:text-slate-300">{card.description}</p>
    </a>
  );
}

export default function CurriculumHome() {
  return (
    <div data-homepage-layout>
      <HubPageShell>
        <HubHero
        badges={['Open-source AI curriculum', 'Beginner to advanced', 'Notebooks, quizzes, cheatsheets']}
        badgeToneClass="text-sky-100/90"
        eyebrow="Zero to AI"
        eyebrowClass="text-sky-200/80"
        title="Learn AI"
        description="Work through Python, data science, LLMs, agents, evaluation, and production systems in one connected learning path with hands-on notebooks and fast-reference guides."
        actions={[
          { label: 'Start the curriculum', href: '/00-course-setup', variant: 'primary' },
          { label: 'View roadmaps', href: '/33-roadmaps', variant: 'secondary' },
          { label: 'Star on GitHub', href: 'https://github.com/PavanMudigonda/zero-to-ai', variant: 'ghost' },
        ]}
        stats={heroStats}
        backgroundClass="bg-[radial-gradient(circle_at_top_left,_rgba(59,130,246,0.20),_transparent_34%),linear-gradient(135deg,_rgba(15,23,42,0.96),_rgba(30,41,59,0.92))]"
        shadowClass="shadow-[0_30px_80px_rgba(15,23,42,0.22)]"
        statLabelClass="text-sky-200/70"
        statDescriptionClass="text-slate-200/85"
      />

        <section className="mt-12 grid gap-5 lg:grid-cols-3">
          {spotlightCards.map((card) => (
            <HubFeatureCard
              key={card.href}
              feature={{
                eyebrow: card.eyebrow,
                title: card.title,
                description: card.description,
                href: card.href,
                cta: card.cta,
                accent: card.accent,
              }}
            />
          ))}
        </section>

        <section className="mt-14">
          <HubSectionIntro
            eyebrow="Recommended sequence"
            title="Follow the curriculum by phase"
            href="/33-roadmaps"
            hrefLabel="See the visual roadmaps"
            accentClass="text-sky-700 dark:text-sky-400"
          />

          <div className="mt-6 grid gap-5 lg:grid-cols-3">
            {phaseCards.map((card) => (
              <Phase key={card.phase} card={card} />
            ))}
          </div>
        </section>

        <section className="mt-14 grid gap-6 lg:grid-cols-[minmax(0,1.3fr)_minmax(280px,0.8fr)]">
          <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900/60">
            <p className="text-sm font-semibold uppercase tracking-[0.18em] text-sky-700 dark:text-sky-400">Build mode</p>
            <h2 className="mt-2 text-3xl font-bold tracking-tight text-slate-900 dark:text-white">Use the docs the way you actually learn</h2>
            <div className="mt-6 grid gap-4 sm:grid-cols-2">
              {utilityCards.map((card) => (
                <Utility key={card.href} card={card} />
              ))}
            </div>
          </div>

          <div className="rounded-3xl border border-slate-200 bg-[linear-gradient(180deg,rgba(14,165,233,0.08),rgba(15,23,42,0.02))] p-6 shadow-sm dark:border-slate-800 dark:bg-[linear-gradient(180deg,rgba(56,189,248,0.10),rgba(15,23,42,0.30))]">
            <p className="text-sm font-semibold uppercase tracking-[0.18em] text-sky-700 dark:text-sky-400">Quick links</p>
            <ul className="mt-5 space-y-3 text-sm">
              {quickLinks.map((link) => (
                <li key={link.href}>
                  <a href={link.href} className="font-semibold text-slate-950 underline decoration-slate-500 underline-offset-4 hover:text-sky-800 dark:text-white dark:decoration-slate-500 dark:hover:text-sky-300">
                    {link.label}
                  </a>
                </li>
              ))}
            </ul>
            <p className="mt-6 text-sm leading-7 text-slate-800 dark:text-slate-200">This site works best as a progression: use the roadmap for direction, notebooks for practice, and cheatsheets for speed.</p>
          </div>
        </section>
      </HubPageShell>
    </div>
  );
}