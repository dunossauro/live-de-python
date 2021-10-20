import * as React from 'react';
import { IMenuItem, OperationModel } from '../../services';
export interface MenuItemProps {
    item: IMenuItem;
    onActivate?: (item: IMenuItem) => void;
    withoutChildren?: boolean;
}
export declare class MenuItem extends React.Component<MenuItemProps> {
    ref: React.RefObject<HTMLLabelElement>;
    activate: (evt: React.MouseEvent<HTMLElement>) => void;
    componentDidMount(): void;
    componentDidUpdate(): void;
    scrollIntoViewIfActive(): void;
    render(): JSX.Element;
}
export interface OperationMenuItemContentProps {
    item: OperationModel;
}
export declare class OperationMenuItemContent extends React.Component<OperationMenuItemContentProps> {
    ref: React.RefObject<HTMLLabelElement>;
    componentDidUpdate(): void;
    render(): JSX.Element;
}
