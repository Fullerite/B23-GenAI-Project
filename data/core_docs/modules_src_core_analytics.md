# Module src/core/analytics
[# core/analytics](#coreanalytics)

This module provides API to work with analytic services.
Each of the analytic services should define its own engine within the `core/analytics/engines` folder.

Notice, there is no implementation for any analytic services.
You have to create it by yourself.

[## Creating a new analytics engine](#creating-a-new-analytics-engine)

Create a new file within the `engines` folder and expose it from the `index` file.
Let's create a simple engine for Google Analytics.

**core/analytics/engines/ga.ts**

```
export default function sendEvent(event: string, hint?: string, extra?: [...string, Dictionary?]) {  
  ga(event, hint, ...extra);  
};
```

**core/analytics/engines**

```
export { default } from 'core/analytics/engines/ga';
```

## Index

### References

* [AnalyticEngine](src_core_analytics.html#AnalyticEngine)

### Functions

* [send](src_core_analytics.html#send)

## References

### AnalyticEngine

Re-exports [AnalyticEngine](../interfaces/src_core_analytics_interface.AnalyticEngine.html)

## Functions

### send

* send(...args: unknown[]): void

* + Defined in [src/core/analytics/index.ts:21](https://github.com/V4Fire/Core/blob/master/src/core/analytics/index.ts#L21)

  Sends the specified analytic event

  #### Parameters

  + ##### Rest ...args: unknown[]

  #### Returns void