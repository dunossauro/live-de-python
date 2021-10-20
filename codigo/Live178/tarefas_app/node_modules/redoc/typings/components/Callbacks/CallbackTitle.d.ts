import * as React from 'react';
export interface CallbackTitleProps {
    name: string;
    opened?: boolean;
    httpVerb: string;
    deprecated?: boolean;
    className?: string;
    onClick?: () => void;
}
export declare class CallbackTitle extends React.PureComponent<CallbackTitleProps> {
    render(): JSX.Element;
}
