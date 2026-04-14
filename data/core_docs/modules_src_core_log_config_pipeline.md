# Module src/core/log/config/pipeline
## Index

### Functions

* [createPipeline](src_core_log_config_pipeline.html#createPipeline)

## Functions

### createPipeline

* createPipeline(pipelineConfig: [LogPipelineConfig](../interfaces/src_core_log_config_interface.LogPipelineConfig.html)): [CanUndef](index.html#CanUndef)<[LogPipeline](../classes/src_core_log_curator_pipeline.LogPipeline.html)>

* + Defined in [src/core/log/config/pipeline.ts:23](https://github.com/V4Fire/Core/blob/master/src/core/log/config/pipeline.ts#L23)

  Creates a pipeline by using the config
  (returns undefined if there are not enough data to create one)

  #### Parameters

  + ##### pipelineConfig: [LogPipelineConfig](../interfaces/src_core_log_config_interface.LogPipelineConfig.html)

  #### Returns [CanUndef](index.html#CanUndef)<[LogPipeline](../classes/src_core_log_curator_pipeline.LogPipeline.html)>