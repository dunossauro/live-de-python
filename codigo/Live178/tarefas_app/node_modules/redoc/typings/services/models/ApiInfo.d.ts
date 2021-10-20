import { OpenAPIContact, OpenAPIInfo, OpenAPILicense } from '../../types';
import { OpenAPIParser } from '../OpenAPIParser';
export declare class ApiInfoModel implements OpenAPIInfo {
    private parser;
    title: string;
    version: string;
    description: string;
    summary: string;
    termsOfService?: string;
    contact?: OpenAPIContact;
    license?: OpenAPILicense;
    downloadLink?: string;
    downloadFileName?: string;
    constructor(parser: OpenAPIParser);
    private getDownloadLink;
    private getDownloadFileName;
}
