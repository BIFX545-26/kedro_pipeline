from kedro.pipeline import Pipeline, node, pipeline
from .nodes import calculate_gc_content


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=calculate_gc_content,
            inputs="raw_sequences",
            outputs="analyzed_sequences",
            name="gc_calc_node",
        )
    ])
