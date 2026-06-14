import { HubFeatureCard, HubHero, HubPageShell, HubSectionIntro } from '@/components/HubPage';

type CheatsheetCategory = {
  title: string;
  href: string;
  description: string;
  eyebrow?: string;
};

type FeaturedCheatsheet = {
  title: string;
  href: string;
  description: string;
  accent: string;
  cta: string;
};

type CheatsheetCollection = {
  title: string;
  description: string;
  accent: string;
  items: CheatsheetCategory[];
};

const featuredCheatsheets: FeaturedCheatsheet[] = [
  {
    title: 'Docker and containers',
    href: '/32-cheatsheets/docker',
    description: 'Modern Docker, Compose, BuildKit, and container workflow references for day-to-day development.',
    accent: 'text-sky-600 dark:text-sky-400',
    cta: 'Open Docker references',
  },
  {
    title: 'Cloud and Terraform',
    href: '/32-cheatsheets/cloud',
    description: 'AWS, Azure, GCP, and Terraform commands for infrastructure, automation, and deployment tasks.',
    accent: 'text-emerald-600 dark:text-emerald-400',
    cta: 'Browse cloud references',
  },
];

const collections: CheatsheetCollection[] = [
  {
    title: 'Platform and infrastructure',
    description: 'Core operational references for cloud, containers, orchestration, and systems work.',
    accent: 'hover:ring-sky-300',
    items: [
      {
        title: 'Cloud CLIs',
        href: '/32-cheatsheets/cloud',
        description: 'AWS, Azure, GCP CLI commands and Terraform workflows.',
      },
      {
        title: 'Docker',
        href: '/32-cheatsheets/docker',
        description: 'Docker commands, Compose workflows, and demo apps.',
      },
      {
        title: 'Kubernetes',
        href: '/32-cheatsheets/k8s',
        description: 'kubectl, Helm, YAML examples, and cluster workflows.',
      },
      {
        title: 'Linux',
        href: '/32-cheatsheets/linux',
        description: 'Linux command references for everyday shell work.',
      },
      {
        title: 'Networking',
        href: '/32-cheatsheets/networking',
        description: 'Networking fundamentals and troubleshooting references.',
      },
      {
        title: 'Monitoring',
        href: '/32-cheatsheets/monitoring',
        description: 'Prometheus and Grafana dashboards, alerts, and metrics.',
      },
    ],
  },
  {
    title: 'Developer workflow and delivery',
    description: 'References that help you ship faster across source control, CI/CD, and automation.',
    accent: 'hover:ring-emerald-300',
    items: [
      {
        title: 'Git',
        href: '/32-cheatsheets/git',
        description: 'Git commands, workflows, and common recovery patterns.',
      },
      {
        title: 'GitHub Actions',
        href: '/32-cheatsheets/github-actions',
        description: 'CI/CD pipelines, runners, and workflow examples.',
      },
      {
        title: 'GitHub CLI',
        href: '/32-cheatsheets/github-cli',
        description: 'gh commands for pull requests, issues, and repo automation.',
      },
      {
        title: 'Jenkins',
        href: '/32-cheatsheets/jenkins',
        description: 'Pipelines, shared libraries, and migration-oriented references.',
      },
      {
        title: 'Shell scripting',
        href: '/32-cheatsheets/shell-scripting',
        description: 'Bash, YAML, JSON, PowerShell, and automation snippets.',
      },
      {
        title: 'Config management',
        href: '/32-cheatsheets/config-management',
        description: 'Ansible and related automation patterns.',
      },
    ],
  },
  {
    title: 'Architecture, data, and interview prep',
    description: 'Reference material for system thinking, storage, and practice loops.',
    accent: 'hover:ring-amber-300',
    items: [
      {
        title: 'Databases',
        href: '/32-cheatsheets/databases',
        description: 'SQL and database quick-reference material.',
      },
      {
        title: 'Interview prep',
        href: '/32-cheatsheets/interview-prep',
        description: 'Scenario-based Linux, Docker, Kubernetes, networking, and CI/CD practice sets.',
      },
    ],
  },
];

const updatedLinks: CheatsheetCategory[] = [
  {
    title: 'Docker commands cheatsheet',
    href: '/32-cheatsheets/docker/docker-commands-cheatsheet',
    description: 'Updated for modern Compose watch, Docker Scout, Docker Debug, and BuildKit-first workflows.',
  },
  {
    title: 'Terraform commands cheatsheet',
    href: '/32-cheatsheets/cloud/terraform-commands-cheatsheet',
    description: 'Refresh-only workflows and newer GitHub Actions examples.',
  },
  {
    title: 'YAML cheatsheet',
    href: '/32-cheatsheets/shell-scripting/yaml-cheatsheet',
    description: 'Current GitHub Actions versions and modern Node matrix examples.',
  },
  {
    title: 'Jenkins cheatsheet',
    href: '/32-cheatsheets/jenkins/jenkins-cheatsheet',
    description: 'Pipeline references with corrected Actions migration snippets.',
  },
];

function CollectionCard({ collection }: { collection: CheatsheetCollection }) {
  return (
    <div className="rounded-3xl border border-slate-200 bg-slate-50 p-6 dark:border-slate-800 dark:bg-slate-900/50">
      <h3 className="text-2xl font-bold text-slate-900 dark:text-white">{collection.title}</h3>
      <p className="mt-3 text-sm leading-7 text-slate-600 dark:text-slate-300">{collection.description}</p>
      <div className="mt-5 grid gap-3">
        {collection.items.map((item) => (
          <a
            key={item.href}
            href={item.href}
            className={`rounded-2xl bg-white px-4 py-4 ring-1 ring-slate-200 transition dark:bg-slate-950 dark:ring-slate-700 ${collection.accent}`}
          >
            <div className="flex items-center justify-between gap-3">
              <div>
                <div className="flex items-center gap-2">
                  <p className="text-base font-semibold text-slate-900 dark:text-slate-100">{item.title}</p>
                  {item.eyebrow ? (
                    <span className="rounded-full bg-sky-100 px-2 py-0.5 text-xs font-semibold uppercase tracking-[0.14em] text-sky-800 dark:bg-sky-950 dark:text-sky-200">
                      {item.eyebrow}
                    </span>
                  ) : null}
                </div>
                <p className="mt-1 text-sm leading-6 text-slate-600 dark:text-slate-300">{item.description}</p>
              </div>
              <span className="text-sm font-semibold text-slate-500 dark:text-slate-400">Open</span>
            </div>
          </a>
        ))}
      </div>
    </div>
  );
}

export default function CheatsheetsHub() {
  return (
    <HubPageShell>
      <HubHero
        badges={['Command-first references', 'DevOps, cloud, data', 'Built for fast lookup']}
        badgeToneClass="text-sky-100/90"
        eyebrow="Cheatsheets"
        eyebrowClass="text-sky-200/80"
        title="Find the command, workflow, or architecture reference fast."
        description="Browse container, cloud, CI/CD, shell, monitoring, and database references without digging through long tutorials."
        actions={[
          { label: 'Open Docker', href: '/32-cheatsheets/docker', variant: 'primary' },
          { label: 'Browse Cloud', href: '/32-cheatsheets/cloud', variant: 'secondary' },
          { label: 'Open GitHub Actions', href: '/32-cheatsheets/github-actions', variant: 'ghost' },
        ]}
        stats={[
          {
            label: 'Coverage',
            value: '15 topic groups',
            description: 'From Docker and Kubernetes to Jenkins, SQL, and interview prep.',
          },
          {
            label: 'Best for',
            value: 'Build while reading',
            description: 'Keep references open next to your terminal, IDE, or notebook instead of context-switching to external docs.',
          },
          {
            label: 'Recently refreshed',
            value: 'Docker, Terraform, YAML',
            description: 'Several operational references were updated to newer tools and current command patterns.',
          },
        ]}
        backgroundClass="bg-[radial-gradient(circle_at_top_left,_rgba(14,165,233,0.18),_transparent_36%),linear-gradient(135deg,_rgba(12,18,32,0.98),_rgba(20,35,55,0.92))]"
        shadowClass="shadow-[0_30px_80px_rgba(15,23,42,0.18)]"
        statLabelClass="text-sky-200/70"
        statDescriptionClass="text-slate-200/85"
      />

      <section className="mt-12 grid gap-5 lg:grid-cols-3">
        {featuredCheatsheets.map((item) => (
          <HubFeatureCard
            key={item.href}
            feature={{
              eyebrow: 'Featured',
              title: item.title,
              description: item.description,
              href: item.href,
              cta: item.cta,
              accent: item.accent,
            }}
          />
        ))}
      </section>

      <section className="mt-14">
        <HubSectionIntro
          eyebrow="Browse by workflow"
          title="Choose the reference set you need"
          href="/31-ai-powered-dev-tools"
          hrefLabel="Continue into AI-powered dev tools"
          accentClass="text-sky-700 dark:text-sky-400"
        />

        <div className="mt-6 grid gap-5 lg:grid-cols-3">
          {collections.map((collection) => (
            <CollectionCard key={collection.title} collection={collection} />
          ))}
        </div>
      </section>

      <section className="mt-14 grid gap-6 lg:grid-cols-[minmax(0,1.2fr)_minmax(280px,0.85fr)]">
        <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900/60">
          <p className="text-sm font-semibold uppercase tracking-[0.18em] text-sky-700 dark:text-sky-400">Freshly updated</p>
          <h2 className="mt-2 text-3xl font-bold tracking-tight text-slate-900 dark:text-white">Start with the newest operational references</h2>
          <div className="mt-6 grid gap-4">
            {updatedLinks.map((item) => (
              <a
                key={item.href}
                href={item.href}
                className="rounded-2xl border border-slate-200 p-5 transition hover:border-sky-300 hover:bg-sky-50/60 dark:border-slate-800 dark:hover:border-sky-800 dark:hover:bg-slate-800/60"
              >
                <h3 className="text-lg font-semibold text-slate-900 dark:text-white">{item.title}</h3>
                <p className="mt-2 text-sm leading-7 text-slate-600 dark:text-slate-300">{item.description}</p>
              </a>
            ))}
          </div>
        </div>

        <div className="rounded-3xl border border-slate-300 bg-[linear-gradient(180deg,#eff6ff,#dbe4f0)] p-6 text-slate-950 shadow-sm dark:border-slate-700 dark:bg-[linear-gradient(180deg,rgba(30,41,59,0.96),rgba(15,23,42,0.92))] dark:text-slate-100">
          <p className="text-sm font-semibold uppercase tracking-[0.18em] text-sky-700 dark:text-sky-300">How to use this hub</p>
          <ul className="mt-5 space-y-3 text-sm !text-slate-800 dark:!text-slate-200">
            <li>Open one category for broad navigation when you are exploring a new tool area.</li>
            <li>Jump straight to a specific cheatsheet when you need a command pattern during implementation.</li>
            <li>Use these references alongside notebooks and project work, not as a separate study track.</li>
          </ul>
          <p className="mt-6 text-sm leading-7 !text-slate-700 dark:!text-slate-200">The best use case for this section is active work: terminal open, docs nearby, and just enough reference material to keep momentum.</p>
        </div>
      </section>
    </HubPageShell>
  );
}