import * as React from 'react';
import { OperationModel } from '../../services/models';
export interface OperationProps {
    operation: OperationModel;
}
export declare class Operation extends React.Component<OperationProps> {
    render(): JSX.Element;
}
