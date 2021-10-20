import * as React from 'react';
declare class IntShelfIcon extends React.PureComponent<{
    className?: string;
    float?: 'left' | 'right';
    size?: string;
    color?: string;
    direction: 'left' | 'right' | 'up' | 'down';
    style?: React.CSSProperties;
}> {
    render(): JSX.Element;
}
export declare const ShelfIcon: import("styled-components").StyledComponent<typeof IntShelfIcon, import("../theme").ResolvedThemeInterface, {}, never>;
export declare const Badge: import("styled-components").StyledComponent<"span", import("../theme").ResolvedThemeInterface, {
    type: string;
}, never>;
export {};
