import * as React from 'react';
export interface FieldDetailProps {
    value?: any;
    label: string;
    raw?: boolean;
}
export declare class FieldDetail extends React.PureComponent<FieldDetailProps> {
    render(): JSX.Element | null;
}
