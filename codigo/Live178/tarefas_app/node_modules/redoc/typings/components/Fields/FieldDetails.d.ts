import * as React from 'react';
import { FieldProps } from './Field';
export declare class FieldDetails extends React.PureComponent<FieldProps, {
    patternShown: boolean;
}> {
    state: {
        patternShown: boolean;
    };
    static contextType: React.Context<import("../..").RedocNormalizedOptions>;
    togglePattern: () => void;
    render(): JSX.Element;
}
