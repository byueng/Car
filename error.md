# Two page replict
- Error: The error occurs when the same component is rendered multiple times during navigation. This can happen if a component is being mounted repeatedly or if it's not being properly replaced when the route changes, causing duplicate instances of the component to appear on the page.
- Fix: In one `<template>` tag just add one pair of `<router-view>`.


# Page doesn't remove wrong
- Error: The error manifests as: after clicking the navigation button, the URL updates, but the page content doesn't change accordingly. This usually happens because the parent component (e.g., Homepage.vue) is not properly unmounted or updated, causing the new component to not render correctly.
- Fix: Use `router` tag: `v-if="$route.path == '/'"` to check out the url.