import * as React from 'react';
import { CallbackModel } from '../../services/models';
export interface CallbacksListProps {
    callbacks: CallbackModel[];
}
export declare class CallbacksList extends React.PureComponent<CallbacksListProps> {
    render(): JSX.Element | null;
}
