import { FinalizationRegistry as FinalizationRegistryMaybeUndefined } from "./FinalizationRegistryWrapper";
import { createReactionCleanupTrackingUsingFinalizationRegister } from "./createReactionCleanupTrackingUsingFinalizationRegister";
import { createTimerBasedReactionCleanupTracking } from "./createTimerBasedReactionCleanupTracking";
var _a = FinalizationRegistryMaybeUndefined
    ? createReactionCleanupTrackingUsingFinalizationRegister(FinalizationRegistryMaybeUndefined)
    : createTimerBasedReactionCleanupTracking(), addReactionToTrack = _a.addReactionToTrack, recordReactionAsCommitted = _a.recordReactionAsCommitted, resetCleanupScheduleForTests = _a.resetCleanupScheduleForTests, forceCleanupTimerToRunNowForTests = _a.forceCleanupTimerToRunNowForTests;
export { addReactionToTrack, recordReactionAsCommitted, resetCleanupScheduleForTests, forceCleanupTimerToRunNowForTests };
//# sourceMappingURL=reactionCleanupTracking.js.map