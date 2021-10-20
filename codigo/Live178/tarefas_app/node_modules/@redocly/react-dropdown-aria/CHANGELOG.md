# react-dropdown-aria

## 2.0.7
- Make dropdown open by pressing space (Only when not searchable) [#45](https://github.com/jfangrad/react-dropdown-aria/pull/45)
- Add button role to top level div to improve keyboard navigation [#45](https://github.com/jfangrad/react-dropdown-aria/pull/45)

## 2.0.6
- Fix markup issues with ul but no li children (ul is now just a div)
- Fix screen readers not reading out the name of element focused when keyboard nav
- Fixed crashing issue when using keyboard nav with grouped options

## 2.0.5
- Fix id being applied to both the input and top level div
- Fix type generation during rollup build

## 2.0.4
- Fix typings not being built properly

## 2.0.2
- Fix issue where group headings with no children matching search would still show
- Add `es` module version (Use rollup to create `commonjs` and `es` versions)
- Fix error in `useId` hook causing SSR to not work
- More file consolidation

## 2.0.1
Mostly codebase changes. Some file organization and consolidation in an attempt to bring bundle size down

## 2.0.0
This release brings a lot of changes to `react-dropdown-aria`, some of these changes are to the api so be sure to read the changelog carefully when upgrading to ensure smooth upgrade!
### Breaking changes
#### Prop changes
- `setSelected` => `onChange`
- `selectedOption` => `value`
- `buttonClassName` => `className`

### New Features
- Search
  - Search is now much nicer (input will show what you are searching)
  - While searching press "tab" to autocomplete


### Changes
- Better accessability
- Added `defaultOpen` prop to control default open state of the dropdown
