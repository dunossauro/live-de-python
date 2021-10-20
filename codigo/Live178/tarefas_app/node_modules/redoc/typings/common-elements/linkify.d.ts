/// <reference types="react" />
export declare const linkifyMixin: (className: any) => import("styled-components").FlattenInterpolation<import("styled-components").ThemedStyledProps<object, import("../theme").ResolvedThemeInterface>>;
export declare function Link(props: {
    to: string;
    className?: string;
    children?: any;
}): JSX.Element | null;
export declare function ShareLink(props: {
    to: string;
}): JSX.Element;
