/// <reference types="react" />
import * as marked from 'marked';
import { AppStore } from './AppStore';
import { RedocNormalizedOptions } from './RedocNormalizedOptions';
export declare const LEGACY_REGEXP = "^ {0,3}<!-- ReDoc-Inject:\\s+?<({component}).*?/?>\\s+?-->\\s*$";
export declare const MDX_COMPONENT_REGEXP: string;
export declare const COMPONENT_REGEXP: string;
export interface MDXComponentMeta {
    component: React.ComponentType;
    propsSelector: (store?: AppStore) => any;
    props?: object;
}
export interface MarkdownHeading {
    id: string;
    name: string;
    level: number;
    items?: MarkdownHeading[];
    description?: string;
}
export declare function buildComponentComment(name: string): string;
export declare class MarkdownRenderer {
    options?: RedocNormalizedOptions | undefined;
    static containsComponent(rawText: string, componentName: string): boolean;
    static getTextBeforeHading(md: string, heading: string): string;
    headings: MarkdownHeading[];
    currentTopHeading: MarkdownHeading;
    private headingEnhanceRenderer;
    private originalHeadingRule;
    constructor(options?: RedocNormalizedOptions | undefined);
    saveHeading(name: string, level: number, container?: MarkdownHeading[], parentId?: string): MarkdownHeading;
    flattenHeadings(container?: MarkdownHeading[]): MarkdownHeading[];
    attachHeadingsDescriptions(rawText: string): void;
    headingRule: (text: string, level: 1 | 2 | 3 | 4 | 5 | 6, raw: string, slugger: marked.Slugger) => string;
    renderMd(rawText: string, extractHeadings?: boolean): string;
    extractHeadings(rawText: string): MarkdownHeading[];
    renderMdWithComponents(rawText: string): Array<string | MDXComponentMeta>;
}
