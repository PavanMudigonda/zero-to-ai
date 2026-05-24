create table if not exists public.learning_progress (
  user_id uuid not null references auth.users (id) on delete cascade,
  route text not null,
  created_at timestamptz not null default timezone('utc', now()),
  primary key (user_id, route)
);

alter table public.learning_progress enable row level security;

drop policy if exists "Users can read their own learning progress" on public.learning_progress;
create policy "Users can read their own learning progress"
on public.learning_progress
for select
to authenticated
using (auth.uid() = user_id);

drop policy if exists "Users can insert their own learning progress" on public.learning_progress;
create policy "Users can insert their own learning progress"
on public.learning_progress
for insert
to authenticated
with check (auth.uid() = user_id);

drop policy if exists "Users can update their own learning progress" on public.learning_progress;
create policy "Users can update their own learning progress"
on public.learning_progress
for update
to authenticated
using (auth.uid() = user_id)
with check (auth.uid() = user_id);

drop policy if exists "Users can delete their own learning progress" on public.learning_progress;
create policy "Users can delete their own learning progress"
on public.learning_progress
for delete
to authenticated
using (auth.uid() = user_id);