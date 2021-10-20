import * as React from 'react';
import { MediaContentModel } from '../../services';
import { FieldModel, RequestBodyModel } from '../../services/models';
export interface ParametersProps {
    parameters?: FieldModel[];
    body?: RequestBodyModel;
}
export declare class Parameters extends React.PureComponent<ParametersProps> {
    orderParams(params: FieldModel[]): Record<string, FieldModel[]>;
    render(): JSX.Element | null;
}
export declare function BodyContent(props: {
    content: MediaContentModel;
    description?: string;
}): JSX.Element;
