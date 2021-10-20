/// <reference types="react" />
import { RedocRawOptions } from '../services/RedocNormalizedOptions';
export interface RedocStandaloneProps {
    spec?: object;
    specUrl?: string;
    options?: RedocRawOptions;
    onLoaded?: (e?: Error) => any;
}
export declare const RedocStandalone: (props: RedocStandaloneProps) => JSX.Element;
