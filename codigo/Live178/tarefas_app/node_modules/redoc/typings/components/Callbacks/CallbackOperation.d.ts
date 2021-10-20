import * as React from 'react';
import { OperationModel } from '../../services/models';
export declare class CallbackOperation extends React.Component<{
    callbackOperation: OperationModel;
}> {
    toggle: () => void;
    render(): JSX.Element;
}
