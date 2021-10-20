/// <reference types="react" />
export interface DropdownOption {
    idx: number;
    value: string;
}
export interface DropdownProps {
    options: DropdownOption[];
    value: string;
    onChange: (option: DropdownOption) => void;
    ariaLabel: string;
}
export declare const StyledDropdown: import("styled-components").StyledComponent<{
    (props: import("@redocly/react-dropdown-aria").DropdownProps): JSX.Element;
    defaultProps: {
        ariaDescribedBy: null;
        ariaLabel: null;
        ariaLabelledBy: null;
        arrowRenderer: undefined;
        centerText: boolean;
        className: undefined;
        contentClassName: null;
        defaultOpen: boolean;
        disabled: boolean;
        height: null;
        hideArrow: boolean;
        id: null;
        maxContentHeight: number;
        openUp: boolean;
        optionItemRenderer: undefined;
        pageKeyTraverseSize: number;
        placeholder: string;
        searchable: boolean;
        selectedValueClassName: null;
        style: {};
        value: undefined;
        width: null;
    };
}, import("../theme").ResolvedThemeInterface, {}, never>;
export declare const SimpleDropdown: import("styled-components").StyledComponent<{
    (props: import("@redocly/react-dropdown-aria").DropdownProps): JSX.Element;
    defaultProps: {
        ariaDescribedBy: null;
        ariaLabel: null;
        ariaLabelledBy: null;
        arrowRenderer: undefined;
        centerText: boolean;
        className: undefined;
        contentClassName: null;
        defaultOpen: boolean;
        disabled: boolean;
        height: null;
        hideArrow: boolean;
        id: null;
        maxContentHeight: number;
        openUp: boolean;
        optionItemRenderer: undefined;
        pageKeyTraverseSize: number;
        placeholder: string;
        searchable: boolean;
        selectedValueClassName: null;
        style: {};
        value: undefined;
        width: null;
    };
}, import("../theme").ResolvedThemeInterface, {}, never>;
export declare const MimeLabel: import("styled-components").StyledComponent<"span", import("../theme").ResolvedThemeInterface, {}, never>;
