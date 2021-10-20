import { OpenAPIPath, Referenced } from '../../types';
import { OpenAPIParser } from '../OpenAPIParser';
import { OperationModel } from './Operation';
import { RedocNormalizedOptions } from '../RedocNormalizedOptions';
export declare class WebhookModel {
    operations: OperationModel[];
    constructor(parser: OpenAPIParser, options: RedocNormalizedOptions, infoOrRef?: Referenced<OpenAPIPath>);
    initWebhooks(parser: OpenAPIParser, webhooks: OpenAPIPath, options: RedocNormalizedOptions): void;
}
