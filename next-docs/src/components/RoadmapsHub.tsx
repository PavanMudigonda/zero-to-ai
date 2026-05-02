import { HubFeatureCard, HubHero, HubPageShell, HubSectionIntro } from '@/components/HubPage';

type HubLink = {
  label: string;
  href: string;
};

type RoadmapGroup = {
  title: string;
  description: string;
  accent: string;
  links: HubLink[];
};

const heroStats = [
  {
    label: 'Coverage',
    value: '4 roadmap sets',
    description: 'From big-picture orientation through system architecture and end-to-end production flows.',
  },
  {
    label: 'Best use',
    value: 'Direction before depth',
    description: 'Use roadmaps to decide what to study next before diving into notebooks, quizzes, or references.',
  },
  {
    label: 'Supports',
    value: 'Curriculum navigation',
    description: 'Connect high-level system views back to the main learning path, cheatsheets, and implementation phases.',
  },
];

const featuredRoadmaps = [
  {
    eyebrow: 'Big picture',
    title: 'Overview maps',
    description: 'Start with the broad AI landscape, machine learning paradigms, deep learning families, and LLM pipelines.',
    href: '/33-roadmaps/01_overview',
    cta: 'Open overview roadmaps',
    accent: 'text-sky-600 dark:text-sky-400',
  },
  {
    eyebrow: 'Systems thinking',
    title: 'Core systems maps',
    description: 'See how vector databases, RAG, MLOps, and deployment patterns fit together at the platform level.',
    href: '/33-roadmaps/02_core_systems',
    cta: 'Explore system maps',
    accent: 'text-emerald-600 dark:text-emerald-400',
  },
  {
    eyebrow: 'Execution flow',
    title: 'End-to-end flows',
    description: 'Follow complete paths from data and modeling to evaluation, shipping, and production operation.',
    href: '/33-roadmaps/04_end_to_end_flows',
    cta: 'See end-to-end flows',
    accent: 'text-amber-600 dark:text-amber-400',
  },
];

const roadmapGroups: RoadmapGroup[] = [
  {
    title: 'Orientation and mental models',
    description: 'Use these maps when you need the overall shape of the field before choosing a specific phase or tool track.',
    accent: 'hover:ring-sky-300',
    links: [
      { label: 'Overview', href: '/33-roadmaps/01_overview' },
      { label: 'Core systems', href: '/33-roadmaps/02_core_systems' },
    ],
  },
  {
    title: 'Advanced capability maps',
    description: 'Jump here when you want a structured view of fine-tuning, multimodal systems, agents, and evaluation.',
    accent: 'hover:ring-emerald-300',
    links: [
      { label: 'Advanced topics', href: '/33-roadmaps/03_advanced_topics' },
      { label: 'AI agents phase', href: '/15-ai-agents' },
      { label: 'Model evaluation phase', href: '/16-model-evaluation' },
    ],
  },
  {
    title: 'Project and production sequencing',
    description: 'Use these routes when you want to understand how complete AI systems move from ideas to deployed workflows.',
    accent: 'hover:ring-amber-300',
    links: [
      { label: 'End-to-end flows', href: '/33-roadmaps/04_end_to_end_flows' },
      { label: 'MLOps phase', href: '/09-mlops' },
      { label: 'Cheatsheets', href: '/32-cheatsheets' },
    ],
  },
];

function GroupCard({ group }: { group: RoadmapGroup }) {
  return (
    <div className="rounded-3xl border border-slate-200 bg-slate-50 p-6 dark:border-slate-800 dark:bg-slate-900/50">
      <h3 className="text-2xl font-bold text-slate-900 dark:text-white">{group.title}</h3>
      <p className="mt-3 text-sm leading-7 text-slate-600 dark:text-slate-300">{group.description}</p>
      <div className="mt-5 flex flex-wrap gap-3 text-sm">
        {group.links.map((link) => (
          <a
            key={link.href}
            href={link.href}
            className={`rounded-full bg-white px-4 py-2 font-medium text-slate-800 ring-1 ring-slate-200 transition dark:bg-slate-950 dark:text-slate-100 dark:ring-slate-700 ${group.accent}`}
          >
            {link.label}
          </a>
        ))}
      </div>
    </div>
  );
}

export default function RoadmapsHub() {
  return (
    <HubPageShell>
      <HubHero
        badges={['Visual learning maps', 'Direction before implementation', 'AI, ML, and production systems']}
        badgeToneClass="text-violet-100/90"
        eyebrow="Roadmaps"
        eyebrowClass="text-violet-200/80"
        title="Use the maps to decide where to go next."
        description="These roadmaps compress the field into high-signal visual guides so you can orient yourself quickly before dropping into notebooks, references, and project work."
        actions={[
          { label: 'Open overview', href: '/33-roadmaps/01_overview', variant: 'primary' },
          { label: 'See core systems', href: '/33-roadmaps/02_core_systems', variant: 'secondary' },
          { label: 'View end-to-end flows', href: '/33-roadmaps/04_end_to_end_flows', variant: 'ghost' },
        ]}
        stats={heroStats}
        backgroundClass="bg-[radial-gradient(circle_at_top_left,_rgba(139,92,246,0.18),_transparent_34%),linear-gradient(135deg,_rgba(17,24,39,0.98),_rgba(36,25,62,0.92))]"
        shadowClass="shadow-[0_30px_80px_rgba(17,24,39,0.22)]"
        statLabelClass="text-violet-200/70"
        statDescriptionClass="text-slate-200/85"
      />

      <section className="mt-12 grid gap-5 lg:grid-cols-3">
        {featuredRoadmaps.map((item) => (
          <HubFeatureCard key={item.href} feature={item} />
        ))}
      </section>

      <section className="mt-14">
        <HubSectionIntro
          eyebrow="Navigate by intent"
          title="Choose the map that matches your current question"
          href="/"
          hrefLabel="Return to the main curriculum"
          accentClass="text-violet-700 dark:text-violet-400"
        />

        <div className="mt-6 grid gap-5 lg:grid-cols-3">
          {roadmapGroups.map((group) => (
            <GroupCard key={group.title} group={group} />
          ))}
        </div>
      </section>
    </HubPageShell>
  );
}