/// <reference types="react" />
import { ExampleModel } from '../../services/models';
export interface ExampleProps {
    example: ExampleModel;
    mimeType: string;
}
export declare function Example({ example, mimeType }: ExampleProps): JSX.Element;
export declare function ExternalExample({ example, mimeType }: ExampleProps): JSX.Element;
