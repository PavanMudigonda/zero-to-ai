'use client';
import dynamic from 'next/dynamic';

const NotebookViewer = dynamic(() => import('./NotebookViewer'), { ssr: false });

export default function DynamicNotebook(props: any) {
  return <NotebookViewer {...props} />;
}
