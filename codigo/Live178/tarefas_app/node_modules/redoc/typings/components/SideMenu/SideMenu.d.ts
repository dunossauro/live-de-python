import * as React from 'react';
import { IMenuItem, MenuStore } from '../../services/MenuStore';
export declare class SideMenu extends React.Component<{
    menu: MenuStore;
    className?: string;
}> {
    static contextType: React.Context<import("../..").RedocNormalizedOptions>;
    private _updateScroll?;
    render(): JSX.Element;
    activate: (item: IMenuItem) => void;
    private saveScrollUpdate;
}
