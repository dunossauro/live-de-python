export function createTrackingData(reaction) {
    var trackingData = {
        reaction: reaction,
        mounted: false,
        changedBeforeMount: false,
        cleanAt: Date.now() + CLEANUP_LEAKED_REACTIONS_AFTER_MILLIS
    };
    return trackingData;
}
/**
 * The minimum time before we'll clean up a Reaction created in a render
 * for a component that hasn't managed to run its effects. This needs to
 * be big enough to ensure that a component won't turn up and have its
 * effects run without being re-rendered.
 */
export var CLEANUP_LEAKED_REACTIONS_AFTER_MILLIS = 10000;
/**
 * The frequency with which we'll check for leaked reactions.
 */
export var CLEANUP_TIMER_LOOP_MILLIS = 10000;
//# sourceMappingURL=reactionCleanupTrackingCommon.js.map