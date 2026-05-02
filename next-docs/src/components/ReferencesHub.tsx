import { HubFeatureCard, HubHero, HubPageShell, HubSectionIntro } from '@/components/HubPage';

type ReferenceLink = {
  label: string;
  href: string;
};

type ReferenceGroup = {
  title: string;
  description: string;
  accent: string;
  links: ReferenceLink[];
};

const heroStats = [
  {
    label: 'Purpose',
    value: 'Supplemental depth',
    description: 'Use this section for extra explanations, guided labs, and outside practice when the core curriculum is not enough.',
  },
  {
    label: 'Current collection',
    value: 'Microsoft Labs',
    description: 'A curated shelf of beginner-to-intermediate open course material and hands-on projects from Microsoft.',
  },
  {
    label: 'Best workflow',
    value: 'Study, then return',
    description: 'Treat these resources as targeted supplements, not a second curriculum you need to complete end to end.',
  },
];

const featuredResources = [
  {
    eyebrow: 'Hands-on practice',
    title: 'Microsoft Labs',
    description: 'Use the Microsoft course collection for additional structured practice across AI, machine learning, data, LangChain, agents, and MCP.',
    href: '/22-references/microsoft-labs',
    cta: 'Browse Microsoft Labs',
    accent: 'text-sky-600 dark:text-sky-400',
  },
  {
    eyebrow: 'Pair with study',
    title: 'Return to the curriculum',
    description: 'After using an external resource, come back to the main sequence so the extra context gets applied immediately.',
    href: '/',
    cta: 'Go back to the main path',
    accent: 'text-emerald-600 dark:text-emerald-400',
  },
  {
    eyebrow: 'Re-anchor fast',
    title: 'Use cheatsheets and quizzes',
    description: 'Supplemental resources work best when you reconnect them to practical reference material and short understanding checks.',
    href: '/32-cheatsheets',
    cta: 'Open practice supports',
    accent: 'text-amber-600 dark:text-amber-400',
  },
];

const usageGroups: ReferenceGroup[] = [
  {
    title: 'When to come here',
    description: 'Use supplemental resources when you want a second explanation, more guided practice, or a different teaching style for the same topic.',
    accent: 'hover:ring-sky-300',
    links: [
      { label: 'Microsoft Labs', href: '/22-references/microsoft-labs' },
      { label: 'Main curriculum', href: '/' },
      { label: 'Roadmaps', href: '/33-roadmaps' },
    ],
  },
  {
    title: 'How to use it well',
    description: 'Pick the collection that matches your current phase, work through it intentionally, and return to the repo to apply what you learned.',
    accent: 'hover:ring-emerald-300',
    links: [
      { label: 'Python phase', href: '/01-python' },
      { label: 'Data science phase', href: '/02-data-science' },
      { label: 'AI agents phase', href: '/15-ai-agents' },
    ],
  },
  {
    title: 'How to avoid drift',
    description: 'Do not turn references into a second parallel curriculum. Use them to unblock learning, then reconnect to projects and phase work.',
    accent: 'hover:ring-amber-300',
    links: [
      { label: 'Quizzes', href: '/21-quizzes' },
      { label: 'Cheatsheets', href: '/32-cheatsheets' },
      { label: 'Glossary', href: '/23-glossary' },
    ],
  },
];

function GroupCard({ group }: { group: ReferenceGroup }) {
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

export default function ReferencesHub() {
  return (
    <HubPageShell>
      <HubHero
        badges={['Supplemental learning shelf', 'External labs and practice', 'Use selectively, not endlessly']}
        badgeToneClass="text-rose-100/90"
        eyebrow="References"
        eyebrowClass="text-rose-200/80"
        title="Use external resources without losing the main path."
        description="This section is for curated supplemental material that gives you alternate explanations, extra practice, and hands-on labs when you need more depth than the core repo provides."
        actions={[
          { label: 'Open Microsoft Labs', href: '/22-references/microsoft-labs', variant: 'primary' },
          { label: 'Return to the curriculum', href: '/', variant: 'secondary' },
          { label: 'See roadmaps', href: '/33-roadmaps', variant: 'ghost' },
        ]}
        stats={heroStats}
        backgroundClass="bg-[radial-gradient(circle_at_top_left,_rgba(244,63,94,0.18),_transparent_34%),linear-gradient(135deg,_rgba(15,23,42,0.96),_rgba(55,28,44,0.92))]"
        shadowClass="shadow-[0_30px_80px_rgba(15,23,42,0.22)]"
        statLabelClass="text-rose-200/70"
        statDescriptionClass="text-slate-200/85"
      />

      <section className="mt-12 grid gap-5 lg:grid-cols-3">
        {featuredResources.map((item) => (
          <HubFeatureCard key={item.href} feature={item} />
        ))}
      </section>

      <section className="mt-14">
        <HubSectionIntro
          eyebrow="Use references intentionally"
          title="Pick the right supplement for the problem you have now"
          href="/22-references/microsoft-labs"
          hrefLabel="Go straight to Microsoft Labs"
          accentClass="text-rose-700 dark:text-rose-400"
        />

        <div className="mt-6 grid gap-5 lg:grid-cols-3">
          {usageGroups.map((group) => (
            <GroupCard key={group.title} group={group} />
          ))}
        </div>
      </section>
    </HubPageShell>
  );
}