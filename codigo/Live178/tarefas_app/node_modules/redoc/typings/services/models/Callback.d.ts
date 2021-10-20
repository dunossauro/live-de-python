import { OpenAPICallback, Referenced } from '../../types';
import { OpenAPIParser } from '../OpenAPIParser';
import { OperationModel } from './Operation';
import { RedocNormalizedOptions } from '../RedocNormalizedOptions';
export declare class CallbackModel {
    expanded: boolean;
    name: string;
    operations: OperationModel[];
    constructor(parser: OpenAPIParser, name: string, infoOrRef: Referenced<OpenAPICallback>, pointer: string, options: RedocNormalizedOptions);
    toggle(): void;
}
