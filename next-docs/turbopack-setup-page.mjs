"use no memo";

import { createElement } from "react";
import { jsx } from "react/jsx-runtime";
import { useMDXComponents } from "./src/mdx-components.tsx";

export function HOC_MDXWrapper(MDXContent, hocProps) {
  return function MDXWrapper(props) {
    const Wrapper = useMDXComponents().wrapper;
    const children = createElement(MDXContent, props);
    return Wrapper ? jsx(Wrapper, { ...hocProps, children }) : children;
  };
}
