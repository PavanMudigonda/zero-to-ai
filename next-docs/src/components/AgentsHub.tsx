import { HubFeatureCard, HubHero, HubPageShell, HubSectionIntro } from '@/components/HubPage';

type HubLink = {
  label: string;
  href: string;
};

type FeaturedTrack = {
  eyebrow: string;
  title: string;
  description: string;
  href: string;
  cta: string;
  accent: string;
};

type ModuleGroup = {
  title: string;
  description: string;
  accent: string;
  links: HubLink[];
};

type UtilityCard = {
  title: string;
  description: string;
  href: string;
};

const learningSignals = [
  {
    label: 'Focus',
    value: 'Tool-using agents',
    description: 'Move from chatbot-style prompting to systems that plan, call tools, and complete multi-step tasks.',
  },
  {
    label: 'Core topics',
    value: '11 primary modules',
    description: 'Covers function calling, ReAct, frameworks, MCP, reasoning models, evaluation, and production patterns.',
  },
  {
    label: 'Outcome',
    value: 'Build one real agent',
    description: 'The section works best when you build and evaluate one end-to-end agent instead of skimming every framework.',
  },
];

const featuredTracks: FeaturedTrack[] = [
  {
    eyebrow: 'Start here',
    title: 'Enter the phase intentionally',
    description: 'Use the intro and first modules to get the core mental model right before touching agent frameworks.',
    href: '/15-ai-agents/01_START_HERE',
    cta: 'Open start here',
    accent: 'text-sky-600 dark:text-sky-400',
  },
  {
    eyebrow: 'Protocol and platform',
    title: 'Understand MCP and modern stacks',
    description: 'Jump to MCP, SDKs, reasoning models, and the 2026 platform landscape if you already know the basics.',
    href: '/15-ai-agents/07_mcp_model_context_protocol',
    cta: 'Explore modern agent runtimes',
    accent: 'text-emerald-600 dark:text-emerald-400',
  },
  {
    eyebrow: 'Production bar',
    title: 'Measure and harden agents',
    description: 'Agent work becomes real when you evaluate trajectories, inspect tool use, and add safety and observability.',
    href: '/15-ai-agents/11_agent_evaluation',
    cta: 'Go to evaluation',
    accent: 'text-amber-600 dark:text-amber-400',
  },
];

const moduleGroups: ModuleGroup[] = [
  {
    title: 'Foundations and tool use',
    description: 'Learn what agents are, how tool schemas work, and how reasoning plus acting changes the interaction model.',
    accent: 'hover:ring-sky-300',
    links: [
      { label: 'Start Here', href: '/15-ai-agents/01_START_HERE' },
      { label: 'Intro to Agents', href: '/15-ai-agents/02_intro_to_agents' },
      { label: 'Function Calling', href: '/15-ai-agents/03_function_calling' },
      { label: 'ReAct Pattern', href: '/15-ai-agents/04_react_pattern' },
    ],
  },
  {
    title: 'Frameworks, orchestration, and protocols',
    description: 'Compare agent frameworks, coordinate multi-agent workflows, and understand interoperability layers like MCP.',
    accent: 'hover:ring-emerald-300',
    links: [
      { label: 'Agent Frameworks', href: '/15-ai-agents/05_agent_frameworks' },
      { label: 'Multi-Agent Systems', href: '/15-ai-agents/06_multi_agent_systems' },
      { label: 'MCP', href: '/15-ai-agents/07_mcp_model_context_protocol' },
      { label: 'Agents SDK and LangGraph', href: '/15-ai-agents/08_openai_agents_sdk_langgraph' },
    ],
  },
  {
    title: 'Reasoning, evaluation, and the current landscape',
    description: 'Study reasoning models, agentic platforms, evaluation methods, and coding-agent workflows.',
    accent: 'hover:ring-amber-300',
    links: [
      { label: 'Reasoning Models', href: '/15-ai-agents/09_reasoning_models' },
      { label: 'Autonomous Agents 2026', href: '/15-ai-agents/10_autonomous_agents_2026' },
      { label: 'Agent Evaluation', href: '/15-ai-agents/11_agent_evaluation' },
      { label: 'VS Code Agent Debug Logs', href: '/15-ai-agents/12_vscode_agent_debug_logs' },
      { label: 'Agentic Coding IDEs', href: '/15-ai-agents/13_agentic_coding_ides' },
    ],
  },
];

const practiceCards: UtilityCard[] = [
  {
    title: 'Assignment',
    description: 'Build a production-ready agent with tools, error handling, memory, and evaluation.',
    href: '/15-ai-agents/12_assignment',
  },
  {
    title: 'Challenges',
    description: 'Use the hands-on challenge set to pressure-test design choices and tool-use behavior.',
    href: '/15-ai-agents/13_challenges',
  },
  {
    title: 'Pre-Quiz',
    description: 'Assess baseline knowledge before you go deeper into frameworks and protocols.',
    href: '/15-ai-agents/15_pre-quiz',
  },
  {
    title: 'Post-Quiz',
    description: 'Validate that you can reason about architecture, tool use, and production concerns.',
    href: '/15-ai-agents/14_post-quiz',
  },
];

const nextSteps: HubLink[] = [
  { label: 'Model evaluation and metrics', href: '/16-model-evaluation' },
  { label: 'Debugging and troubleshooting', href: '/17-debugging-troubleshooting' },
  { label: 'AI safety and red teaming', href: '/19-ai-safety-redteaming' },
  { label: 'AI-powered dev tools', href: '/31-ai-powered-dev-tools' },
];

const projectIdeas = [
  'SQL agent: natural language to queries, results, and insights.',
  'Research agent: search, synthesize, and report with sources.',
  'Coding agent: requirements to code, tests, repair, and iteration.',
  'Support agent: retrieve context, respond, and escalate when needed.',
];

function GroupCard({ group }: { group: ModuleGroup }) {
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

function PracticeCard({ item }: { item: UtilityCard }) {
  return (
    <a
      href={item.href}
      className="rounded-2xl border border-slate-200 p-5 transition hover:border-sky-300 hover:bg-sky-50/60 dark:border-slate-800 dark:hover:border-sky-800 dark:hover:bg-slate-800/60"
    >
      <h3 className="text-lg font-semibold text-slate-900 dark:text-white">{item.title}</h3>
      <p className="mt-2 text-sm leading-7 text-slate-600 dark:text-slate-300">{item.description}</p>
    </a>
  );
}

export default function AgentsHub() {
  return (
    <HubPageShell>
      <HubHero
        badges={['Production agent systems', 'Function calling, MCP, evaluation', 'From basics to 2026 landscape']}
        badgeToneClass="text-emerald-50/90"
        eyebrow="AI Agents"
        eyebrowClass="text-emerald-200/80"
        title="Learn to build agents that reason, use tools, and survive production reality."
        description="Work from tool schemas and ReAct loops through MCP, orchestration frameworks, evaluation, and agentic coding platforms without treating the topic like hype-only content."
        actions={[
          { label: 'Start this phase', href: '/15-ai-agents/01_START_HERE', variant: 'primary' },
          { label: 'Jump to MCP', href: '/15-ai-agents/07_mcp_model_context_protocol', variant: 'secondary' },
          { label: 'See evaluation', href: '/15-ai-agents/11_agent_evaluation', variant: 'ghost' },
        ]}
        stats={learningSignals}
        backgroundClass="bg-[radial-gradient(circle_at_top_left,_rgba(16,185,129,0.18),_transparent_34%),linear-gradient(135deg,_rgba(15,23,42,0.96),_rgba(17,24,39,0.94))]"
        shadowClass="shadow-[0_30px_80px_rgba(15,23,42,0.22)]"
        statLabelClass="text-emerald-200/70"
        statDescriptionClass="text-slate-200/85"
      />

      <section className="mt-12 grid gap-5 lg:grid-cols-3">
        {featuredTracks.map((item) => (
          <HubFeatureCard
            key={item.href}
            feature={{
              eyebrow: item.eyebrow,
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
          eyebrow="Phase map"
          title="Follow the agent curriculum in the right order"
          href="/31-ai-powered-dev-tools"
          hrefLabel="Connect this to coding-agent workflows"
          accentClass="text-emerald-700 dark:text-emerald-400"
        />

        <div className="mt-6 grid gap-5 lg:grid-cols-3">
          {moduleGroups.map((group) => (
            <GroupCard key={group.title} group={group} />
          ))}
        </div>
      </section>

      <section className="mt-14 grid gap-6 lg:grid-cols-[minmax(0,1.2fr)_minmax(280px,0.85fr)]">
        <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900/60">
          <p className="text-sm font-semibold uppercase tracking-[0.18em] text-emerald-700 dark:text-emerald-400">Practice and assessment</p>
          <h2 className="mt-2 text-3xl font-bold tracking-tight text-slate-900 dark:text-white">Build one agent and measure it honestly</h2>
          <div className="mt-6 grid gap-4 sm:grid-cols-2">
            {practiceCards.map((item) => (
              <PracticeCard key={item.href} item={item} />
            ))}
          </div>

          <div className="mt-8 rounded-2xl border border-slate-200 bg-slate-50 p-5 dark:border-slate-800 dark:bg-slate-950/60">
            <h3 className="text-lg font-semibold text-slate-900 dark:text-white">Project ideas</h3>
            <ul className="mt-3 space-y-2 text-sm leading-7 text-slate-600 dark:text-slate-300">
              {projectIdeas.map((idea) => (
                <li key={idea}>{idea}</li>
              ))}
            </ul>
          </div>
        </div>

        <div className="rounded-3xl border border-slate-200 bg-[linear-gradient(180deg,rgba(16,185,129,0.08),rgba(15,23,42,0.02))] p-6 shadow-sm dark:border-slate-800 dark:bg-[linear-gradient(180deg,rgba(52,211,153,0.12),rgba(15,23,42,0.30))]">
          <p className="text-sm font-semibold uppercase tracking-[0.18em] text-emerald-700 dark:text-emerald-400">What comes next</p>
          <ul className="mt-5 space-y-3 text-sm">
            {nextSteps.map((link) => (
              <li key={link.href}>
                <a href={link.href} className="font-medium text-slate-900 underline decoration-slate-300 underline-offset-4 hover:text-emerald-700 dark:text-white dark:decoration-slate-700 dark:hover:text-emerald-300">
                  {link.label}
                </a>
              </li>
            ))}
          </ul>
          <p className="mt-6 text-sm leading-7 text-slate-600 dark:text-slate-300">
            Treat this phase as part of the production sequence in the repo: build one useful agent, inspect traces, evaluate trajectories, and then carry those lessons into safety and debugging.
          </p>
        </div>
      </section>
    </HubPageShell>
  );
}