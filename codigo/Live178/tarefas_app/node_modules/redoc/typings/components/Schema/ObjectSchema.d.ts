import * as React from 'react';
import { SchemaModel } from '../../services/models';
import { SchemaProps } from './Schema';
export interface ObjectSchemaProps extends SchemaProps {
    discriminator?: {
        fieldName: string;
        parentSchema: SchemaModel;
    };
}
export declare class ObjectSchema extends React.Component<ObjectSchemaProps> {
    static contextType: React.Context<import("../..").RedocNormalizedOptions>;
    get parentSchema(): SchemaModel;
    render(): JSX.Element;
}
