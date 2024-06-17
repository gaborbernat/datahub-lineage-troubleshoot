from __future__ import annotations

from openlineage.client import OpenLineageClient
from openlineage.client.event_v2 import InputDataset, Job, OutputDataset, Run, RunEvent, RunState
from openlineage.client.generated.dataset_version_dataset import DatasetVersionDatasetFacet
from openlineage.client.generated.nominal_time_run import NominalTimeRunFacet
from openlineage.client.generated.parent_run import ParentRunFacet
from openlineage.client.transport.http import HttpConfig, HttpTransport

events = [
    RunEvent(
        eventTime="2024-06-12T18:00:09.280000+00:00",
        run=Run(
            runId="197b1bd2-14c1-2a9e-6528-7a6e9935b555",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T17:54:01.280000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.280000+00:00",
                )
            },
        ),
        job=Job(namespace="Acquisition", name="Source1"),
        eventType=RunState.COMPLETE,
        outputs=[OutputDataset(namespace="Acquisition", name="Source1.doc.csv", outputFacets={})],
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.644000+00:00",
        run=Run(
            runId="e1cca92c-8269-929e-2c64-29edb4120016",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:09.280000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.644000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="197b1bd2-14c1-2a9e-6528-7a6e9935b555"),
                    job=Job(namespace="Acquisition", name="Source1"),
                ),
            },
        ),
        job=Job(namespace="AuditService", name="Ingest"),
        eventType=RunState.COMPLETE,
        inputs=[InputDataset(namespace="Acquisition", name="Source1.doc.csv", inputFacets={})],
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.650000+00:00",
        run=Run(
            runId="b14514df-ce16-60a8-6a9b-4558d0012677",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="197b1bd2-14c1-2a9e-6528-7a6e9935b555"),
                    job=Job(namespace="Acquisition", name="Source1"),
                )
            },
        ),
        job=Job(namespace="Audit", name="AcquisitionRdf"),
        eventType=RunState.START,
        inputs=[InputDataset(namespace="Acquisition", name="Source1.doc.csv", inputFacets={})],
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.650000+00:00",
        run=Run(
            runId="db0425e5-f2a5-8170-ddf9-9d2fc83a47be",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:09.650000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.650000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="b14514df-ce16-60a8-6a9b-4558d0012677"),
                    job=Job(namespace="Audit", name="AcquisitionRdf"),
                ),
            },
        ),
        job=Job(namespace="Audit", name="AcquisitionRdf"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.714000+00:00",
        run=Run(
            runId="8caa4a6d-2ce3-75db-2820-32c35c25a966",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="db0425e5-f2a5-8170-ddf9-9d2fc83a47be"),
                    job=Job(namespace="Audit", name="AcquisitionRdf"),
                )
            },
        ),
        job=Job(namespace="Audit", name="Beutify"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.714000+00:00",
        run=Run(
            runId="d32ea643-b003-a5bf-a01d-f93a75c10bb3",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:09.714000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.714000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="8caa4a6d-2ce3-75db-2820-32c35c25a966"), job=Job(namespace="Audit", name="Beutify")
                ),
            },
        ),
        job=Job(namespace="Audit", name="Beutify"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.780000+00:00",
        run=Run(
            runId="bef412ba-0f15-ce67-228f-49075e195991",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:09.714000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.780000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="d32ea643-b003-a5bf-a01d-f93a75c10bb3"), job=Job(namespace="Audit", name="Beutify")
                ),
            },
        ),
        job=Job(namespace="Audit", name="MagicSub"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.782000+00:00",
        run=Run(
            runId="61cc12cd-f8de-239a-dd1b-13bbc355ae95",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="a2c181e2-dc0a-f7c5-3553-349a6f36061b"),
                    job=Job(namespace="Microservice", name="MessageRouter"),
                )
            },
        ),
        job=Job(namespace="AuditService", name="GraphWriter"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.782000+00:00",
        run=Run(
            runId="e814ecc6-67e6-3ba8-55db-e2a260f39b50",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:09.782000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.782000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="61cc12cd-f8de-239a-dd1b-13bbc355ae95"),
                    job=Job(namespace="AuditService", name="GraphWriter"),
                ),
            },
        ),
        job=Job(namespace="AuditService", name="GraphWriter"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.791000+00:00",
        run=Run(
            runId="67e30fb5-8a3c-f78c-8b97-9e8ab09e4a5e",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:09.791000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.791000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="6e4759de-8938-21ce-74ea-e17bd2522873"),
                    job=Job(namespace="Microservice", name="Frost"),
                ),
            },
        ),
        job=Job(namespace="Microservice", name="Frost"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.791000+00:00",
        run=Run(
            runId="6e4759de-8938-21ce-74ea-e17bd2522873",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="d32ea643-b003-a5bf-a01d-f93a75c10bb3"), job=Job(namespace="Audit", name="Beutify")
                )
            },
        ),
        job=Job(namespace="Microservice", name="Frost"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.787000+00:00",
        run=Run(
            runId="6eba9ca2-6ab2-ce33-fb1f-72aacb6d2639",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:09.787000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.787000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="511486b3-f86e-a56b-e7a7-c69d32fa30b5"),
                    job=Job(namespace="Microservice", name="Magic"),
                ),
            },
        ),
        job=Job(namespace="Microservice", name="Magic"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.787000+00:00",
        run=Run(
            runId="511486b3-f86e-a56b-e7a7-c69d32fa30b5",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="d32ea643-b003-a5bf-a01d-f93a75c10bb3"), job=Job(namespace="Audit", name="Beutify")
                )
            },
        ),
        job=Job(namespace="Microservice", name="Magic"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.772000+00:00",
        run=Run(
            runId="72eab30f-b2bf-2291-adc6-ddf73c713604",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="d32ea643-b003-a5bf-a01d-f93a75c10bb3"), job=Job(namespace="Audit", name="Beutify")
                )
            },
        ),
        job=Job(namespace="Microservice", name="MessageRouter"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.772000+00:00",
        run=Run(
            runId="a2c181e2-dc0a-f7c5-3553-349a6f36061b",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:09.772000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.772000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="72eab30f-b2bf-2291-adc6-ddf73c713604"),
                    job=Job(namespace="Microservice", name="MessageRouter"),
                ),
            },
        ),
        job=Job(namespace="Microservice", name="MessageRouter"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.956000+00:00",
        run=Run(
            runId="b3215075-ad2f-d345-64ec-b489de2d4fd4",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:09.956000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.956000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="a0439d12-a92a-5ed0-de38-a76344b8bb6a"),
                    job=Job(namespace="Audit", name="AuditWriter"),
                ),
            },
        ),
        job=Job(namespace="Audit", name="AuditWriter"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.956000+00:00",
        run=Run(
            runId="a0439d12-a92a-5ed0-de38-a76344b8bb6a",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="bef412ba-0f15-ce67-228f-49075e195991"), job=Job(namespace="Audit", name="MagicSub")
                )
            },
        ),
        job=Job(namespace="Audit", name="AuditWriter"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.970000+00:00",
        run=Run(
            runId="74915ed7-30bc-82a0-29d3-1f9340cfc08c",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:09.970000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.970000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="c3fdcc5f-d58a-c25f-9374-cab255cd4dc6"),
                    job=Job(namespace="Audit", name="AuditWriter"),
                ),
            },
        ),
        job=Job(namespace="Audit", name="AuditWriter"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.970000+00:00",
        run=Run(
            runId="c3fdcc5f-d58a-c25f-9374-cab255cd4dc6",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="bef412ba-0f15-ce67-228f-49075e195991"), job=Job(namespace="Audit", name="MagicSub")
                )
            },
        ),
        job=Job(namespace="Audit", name="AuditWriter"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.982000+00:00",
        run=Run(
            runId="e43ea1c8-6ed5-026a-508a-1310cf9132e6",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:09.982000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.982000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="ca6be933-179b-5d6d-4eed-e3c06abdcd93"),
                    job=Job(namespace="Audit", name="AuditWriter"),
                ),
            },
        ),
        job=Job(namespace="Audit", name="AuditWriter"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.982000+00:00",
        run=Run(
            runId="ca6be933-179b-5d6d-4eed-e3c06abdcd93",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="bef412ba-0f15-ce67-228f-49075e195991"), job=Job(namespace="Audit", name="MagicSub")
                )
            },
        ),
        job=Job(namespace="Audit", name="AuditWriter"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.988000+00:00",
        run=Run(
            runId="08468e50-5117-b11b-ed83-8623a58e3054",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="bef412ba-0f15-ce67-228f-49075e195991"), job=Job(namespace="Audit", name="MagicSub")
                )
            },
        ),
        job=Job(namespace="Microservice", name="SearchWriter"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:09.988000+00:00",
        run=Run(
            runId="28d53cdf-5c42-5890-4ecf-de2a60aa1228",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:09.988000+00:00",
                    nominalEndTime="2024-06-12T18:00:09.988000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="08468e50-5117-b11b-ed83-8623a58e3054"),
                    job=Job(namespace="Microservice", name="SearchWriter"),
                ),
            },
        ),
        job=Job(namespace="Microservice", name="SearchWriter"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.206000+00:00",
        run=Run(
            runId="db1c6443-c42a-0a8d-f43e-8a964443e3bf",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="197b1bd2-14c1-2a9e-6528-7a6e9935b555"),
                    job=Job(namespace="Acquisition", name="Source1"),
                )
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineTrigger"),
        eventType=RunState.START,
        inputs=[InputDataset(namespace="Acquisition", name="Source1.doc.csv", inputFacets={})],
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.222000+00:00",
        run=Run(
            runId="e6937328-7ce1-6bd0-c406-1e372d2a12e2",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:10.206000+00:00",
                    nominalEndTime="2024-06-12T18:00:10.222000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="db1c6443-c42a-0a8d-f43e-8a964443e3bf"),
                    job=Job(namespace="Pipeline", name="PipelineTrigger"),
                ),
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineTrigger"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.258000+00:00",
        run=Run(
            runId="bd1db55c-a28f-e365-7f04-92d278b08623",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="197b1bd2-14c1-2a9e-6528-7a6e9935b555"),
                    job=Job(namespace="Acquisition", name="Source1"),
                )
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineTrigger"),
        eventType=RunState.START,
        inputs=[InputDataset(namespace="Acquisition", name="Source1.doc.csv", inputFacets={})],
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.273000+00:00",
        run=Run(
            runId="c3b1fd34-a31a-c438-32d3-43239271d658",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:10.258000+00:00",
                    nominalEndTime="2024-06-12T18:00:10.273000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="bd1db55c-a28f-e365-7f04-92d278b08623"),
                    job=Job(namespace="Pipeline", name="PipelineTrigger"),
                ),
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineTrigger"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.285000+00:00",
        run=Run(
            runId="d0908a82-4b4d-32aa-f9fa-ce770c891839",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="e6937328-7ce1-6bd0-c406-1e372d2a12e2"),
                    job=Job(namespace="Pipeline", name="PipelineTrigger"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Extract"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.352000+00:00",
        run=Run(
            runId="2832230f-b5c7-4ff1-f441-916946d5fe3f",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="c3b1fd34-a31a-c438-32d3-43239271d658"),
                    job=Job(namespace="Pipeline", name="PipelineTrigger"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Extract"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.285000+00:00",
        run=Run(
            runId="4a24ae9e-a44d-3ed4-422c-8811ad3e82ac",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:10.285000+00:00",
                    nominalEndTime="2024-06-12T18:00:10.285000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="d0908a82-4b4d-32aa-f9fa-ce770c891839"),
                    job=Job(namespace="CheckFile", name="Extract"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Extract"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.352000+00:00",
        run=Run(
            runId="d58e095b-5c4c-11b0-8fdd-8e6efcb750a5",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:10.352000+00:00",
                    nominalEndTime="2024-06-12T18:00:10.352000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="2832230f-b5c7-4ff1-f441-916946d5fe3f"),
                    job=Job(namespace="CheckFile", name="Extract"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Extract"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.853000+00:00",
        run=Run(
            runId="a15c75c5-c159-8ef6-8dbe-19e35d2963ac",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="4a24ae9e-a44d-3ed4-422c-8811ad3e82ac"),
                    job=Job(namespace="CheckFile", name="Extract"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.915000+00:00",
        run=Run(
            runId="f63d0606-a86e-8fa0-8615-dde75d9c1f88",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="4a24ae9e-a44d-3ed4-422c-8811ad3e82ac"),
                    job=Job(namespace="CheckFile", name="Extract"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.970000+00:00",
        run=Run(
            runId="f4a71764-2bf0-aa3e-18db-3d83a0e6c162",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="d58e095b-5c4c-11b0-8fdd-8e6efcb750a5"),
                    job=Job(namespace="CheckFile", name="Extract"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.935000+00:00",
        run=Run(
            runId="a2dd7252-9cf4-1f83-e8e4-dbfd83961f16",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="4a24ae9e-a44d-3ed4-422c-8811ad3e82ac"),
                    job=Job(namespace="CheckFile", name="Extract"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.001000+00:00",
        run=Run(
            runId="771be46d-defe-bd7c-a7a3-f8fc29cb37c1",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="4a24ae9e-a44d-3ed4-422c-8811ad3e82ac"),
                    job=Job(namespace="CheckFile", name="Extract"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.021000+00:00",
        run=Run(
            runId="c465d63d-94e0-de8b-5885-a7e2d22f189b",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="4a24ae9e-a44d-3ed4-422c-8811ad3e82ac"),
                    job=Job(namespace="CheckFile", name="Extract"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.041000+00:00",
        run=Run(
            runId="e73fe814-d023-e3c4-45ab-f1e6ce4e77f6",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="d58e095b-5c4c-11b0-8fdd-8e6efcb750a5"),
                    job=Job(namespace="CheckFile", name="Extract"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.994000+00:00",
        run=Run(
            runId="5b264618-aace-831a-dc3e-57449797cfb1",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="d58e095b-5c4c-11b0-8fdd-8e6efcb750a5"),
                    job=Job(namespace="CheckFile", name="Extract"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.048000+00:00",
        run=Run(
            runId="9c55d169-3ed1-f763-b776-6eff69897af6",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="4a24ae9e-a44d-3ed4-422c-8811ad3e82ac"),
                    job=Job(namespace="CheckFile", name="Extract"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.116000+00:00",
        run=Run(
            runId="b8b8032d-0258-c055-6d4f-f40f8fea9b42",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="d58e095b-5c4c-11b0-8fdd-8e6efcb750a5"),
                    job=Job(namespace="CheckFile", name="Extract"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.115000+00:00",
        run=Run(
            runId="d6721ec7-c69c-73db-6f83-e5c1620f71ef",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="d58e095b-5c4c-11b0-8fdd-8e6efcb750a5"),
                    job=Job(namespace="CheckFile", name="Extract"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.135000+00:00",
        run=Run(
            runId="ecc65dd5-c31f-f5c2-6c78-dacddf5d6b89",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="d58e095b-5c4c-11b0-8fdd-8e6efcb750a5"),
                    job=Job(namespace="CheckFile", name="Extract"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.135000+00:00",
        run=Run(
            runId="74792b8b-546d-3fa7-a340-28983baed3c3",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:11.135000+00:00",
                    nominalEndTime="2024-06-12T18:00:11.135000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="ecc65dd5-c31f-f5c2-6c78-dacddf5d6b89"),
                    job=Job(namespace="CheckFile", name="Transform"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.048000+00:00",
        run=Run(
            runId="3c6a2e37-4992-327b-6610-e0beb08d4afd",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:11.048000+00:00",
                    nominalEndTime="2024-06-12T18:00:11.048000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="9c55d169-3ed1-f763-b776-6eff69897af6"),
                    job=Job(namespace="CheckFile", name="Transform"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.021000+00:00",
        run=Run(
            runId="5e478212-8509-29b7-96e7-5d49b20f890a",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:11.021000+00:00",
                    nominalEndTime="2024-06-12T18:00:11.021000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="c465d63d-94e0-de8b-5885-a7e2d22f189b"),
                    job=Job(namespace="CheckFile", name="Transform"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.915000+00:00",
        run=Run(
            runId="356ea158-a3c6-264b-ffba-e138450485f9",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:10.915000+00:00",
                    nominalEndTime="2024-06-12T18:00:10.915000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="f63d0606-a86e-8fa0-8615-dde75d9c1f88"),
                    job=Job(namespace="CheckFile", name="Transform"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.041000+00:00",
        run=Run(
            runId="b51fdd25-57e7-1876-aba9-a6482da34dd6",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:11.041000+00:00",
                    nominalEndTime="2024-06-12T18:00:11.041000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="e73fe814-d023-e3c4-45ab-f1e6ce4e77f6"),
                    job=Job(namespace="CheckFile", name="Transform"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.935000+00:00",
        run=Run(
            runId="6e24ad81-6c4b-1dae-1354-c0c836756320",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:10.935000+00:00",
                    nominalEndTime="2024-06-12T18:00:10.935000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="a2dd7252-9cf4-1f83-e8e4-dbfd83961f16"),
                    job=Job(namespace="CheckFile", name="Transform"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.001000+00:00",
        run=Run(
            runId="70d64c04-e8ca-f954-69b9-53889d7e126e",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:11.001000+00:00",
                    nominalEndTime="2024-06-12T18:00:11.001000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="771be46d-defe-bd7c-a7a3-f8fc29cb37c1"),
                    job=Job(namespace="CheckFile", name="Transform"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.853000+00:00",
        run=Run(
            runId="4d027d90-0095-70e4-bce2-cb3612bfca05",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:10.853000+00:00",
                    nominalEndTime="2024-06-12T18:00:10.853000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="a15c75c5-c159-8ef6-8dbe-19e35d2963ac"),
                    job=Job(namespace="CheckFile", name="Transform"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.994000+00:00",
        run=Run(
            runId="611a7aa9-85ea-baba-9eba-7253c5ab8f59",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:10.994000+00:00",
                    nominalEndTime="2024-06-12T18:00:10.994000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="5b264618-aace-831a-dc3e-57449797cfb1"),
                    job=Job(namespace="CheckFile", name="Transform"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.116000+00:00",
        run=Run(
            runId="f7ef0ae4-96c9-735b-d8b3-0ed342822634",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:11.116000+00:00",
                    nominalEndTime="2024-06-12T18:00:11.116000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="b8b8032d-0258-c055-6d4f-f40f8fea9b42"),
                    job=Job(namespace="CheckFile", name="Transform"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:11.115000+00:00",
        run=Run(
            runId="dee6275e-f614-4a1d-6603-216a949dc3bf",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:11.115000+00:00",
                    nominalEndTime="2024-06-12T18:00:11.115000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="d6721ec7-c69c-73db-6f83-e5c1620f71ef"),
                    job=Job(namespace="CheckFile", name="Transform"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:22.913000+00:00",
        run=Run(
            runId="caa8df1a-3ceb-c042-7a43-d4b8e4cf2cb3",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="70d64c04-e8ca-f954-69b9-53889d7e126e"),
                    job=Job(namespace="CheckFile", name="Transform"),
                )
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineMerge"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:22.927000+00:00",
        run=Run(
            runId="0dc3098a-a940-ad3b-2979-4602b3162197",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:22.913000+00:00",
                    nominalEndTime="2024-06-12T18:00:22.927000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="caa8df1a-3ceb-c042-7a43-d4b8e4cf2cb3"),
                    job=Job(namespace="Pipeline", name="PipelineMerge"),
                ),
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineMerge"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:23.024000+00:00",
        run=Run(
            runId="5a48019a-deca-4b75-8ef9-b58af1fc2421",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="0dc3098a-a940-ad3b-2979-4602b3162197"),
                    job=Job(namespace="Pipeline", name="PipelineMerge"),
                )
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineTrigger"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:23.116000+00:00",
        run=Run(
            runId="7f7dd905-aac2-9cbf-7dbf-7372db4e2128",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:23.024000+00:00",
                    nominalEndTime="2024-06-12T18:00:23.116000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="5a48019a-deca-4b75-8ef9-b58af1fc2421"),
                    job=Job(namespace="Pipeline", name="PipelineTrigger"),
                ),
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineTrigger"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:23.177000+00:00",
        run=Run(
            runId="2da545b8-1f73-cc46-8d4e-eb4fbbcacd15",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="0dc3098a-a940-ad3b-2979-4602b3162197"),
                    job=Job(namespace="Pipeline", name="PipelineMerge"),
                )
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineTrigger"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:23.206000+00:00",
        run=Run(
            runId="7e46c4a4-c2a9-48a0-ccf6-dc66c1594f05",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:23.177000+00:00",
                    nominalEndTime="2024-06-12T18:00:23.206000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="2da545b8-1f73-cc46-8d4e-eb4fbbcacd15"),
                    job=Job(namespace="Pipeline", name="PipelineTrigger"),
                ),
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineTrigger"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:23.932000+00:00",
        run=Run(
            runId="c5e9f653-a0be-2c62-a1c2-0aa33845140c",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="7f7dd905-aac2-9cbf-7dbf-7372db4e2128"),
                    job=Job(namespace="Pipeline", name="PipelineTrigger"),
                )
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineMap"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:23.968000+00:00",
        run=Run(
            runId="60511fb3-41d3-c31d-a635-87e4b54ad31b",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="7e46c4a4-c2a9-48a0-ccf6-dc66c1594f05"),
                    job=Job(namespace="Pipeline", name="PipelineTrigger"),
                )
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineMap"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:24.023000+00:00",
        run=Run(
            runId="a358fbee-402c-5a69-146f-df2fbb9e27ff",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:23.968000+00:00",
                    nominalEndTime="2024-06-12T18:00:24.023000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="60511fb3-41d3-c31d-a635-87e4b54ad31b"),
                    job=Job(namespace="Pipeline", name="PipelineMap"),
                ),
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineMap"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:24.048000+00:00",
        run=Run(
            runId="73ee5889-e784-f89c-4614-9674a23db7ea",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="a358fbee-402c-5a69-146f-df2fbb9e27ff"),
                    job=Job(namespace="Pipeline", name="PipelineMap"),
                )
            },
        ),
        job=Job(namespace="Validation", name="validateCatalog"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:24.095000+00:00",
        run=Run(
            runId="751ed3a2-fa96-3d3c-b432-2ddcc29e1313",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:23.932000+00:00",
                    nominalEndTime="2024-06-12T18:00:24.095000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="c5e9f653-a0be-2c62-a1c2-0aa33845140c"),
                    job=Job(namespace="Pipeline", name="PipelineMap"),
                ),
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineMap"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:24.048000+00:00",
        run=Run(
            runId="41fcd4b1-9b22-c94f-d977-dd0cbd8b7ee1",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:24.048000+00:00",
                    nominalEndTime="2024-06-12T18:00:24.048000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="73ee5889-e784-f89c-4614-9674a23db7ea"),
                    job=Job(namespace="Validation", name="validateCatalog"),
                ),
            },
        ),
        job=Job(namespace="Validation", name="validateCatalog"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:26.090000+00:00",
        run=Run(
            runId="0f2404b8-c7dc-d848-6ee5-4a37923476aa",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="41fcd4b1-9b22-c94f-d977-dd0cbd8b7ee1"),
                    job=Job(namespace="Validation", name="validateCatalog"),
                )
            },
        ),
        job=Job(namespace="Validation", name="validateData"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:26.099000+00:00",
        run=Run(
            runId="d8eb8c90-b2f3-1fec-47b7-8483e9cbb726",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="751ed3a2-fa96-3d3c-b432-2ddcc29e1313"),
                    job=Job(namespace="Pipeline", name="PipelineMap"),
                )
            },
        ),
        job=Job(namespace="Validation", name="validateCatalog"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:26.099000+00:00",
        run=Run(
            runId="f57e2cf0-95f3-4a64-5e44-60fa8caf8aca",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:26.099000+00:00",
                    nominalEndTime="2024-06-12T18:00:26.099000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="d8eb8c90-b2f3-1fec-47b7-8483e9cbb726"),
                    job=Job(namespace="Validation", name="validateCatalog"),
                ),
            },
        ),
        job=Job(namespace="Validation", name="validateCatalog"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:26.090000+00:00",
        run=Run(
            runId="de879cf7-2430-1bd6-f7d9-5f3b527f29e0",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:26.090000+00:00",
                    nominalEndTime="2024-06-12T18:00:26.090000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="0f2404b8-c7dc-d848-6ee5-4a37923476aa"),
                    job=Job(namespace="Validation", name="validateData"),
                ),
            },
        ),
        job=Job(namespace="Validation", name="validateData"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:29.935000+00:00",
        run=Run(
            runId="c7d3c528-bab9-6376-729b-f5ac108ba3d0",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="de879cf7-2430-1bd6-f7d9-5f3b527f29e0"),
                    job=Job(namespace="Validation", name="validateData"),
                )
            },
        ),
        job=Job(namespace="CheckFile", name="DataPublisher"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:29.967000+00:00",
        run=Run(
            runId="90737031-3ca8-f6a6-adc3-a6b5297c9385",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="f57e2cf0-95f3-4a64-5e44-60fa8caf8aca"),
                    job=Job(namespace="Validation", name="validateCatalog"),
                )
            },
        ),
        job=Job(namespace="Validation", name="validateData"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:29.935000+00:00",
        run=Run(
            runId="3df12357-a207-53f5-cf9f-731a7e332c33",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:29.935000+00:00",
                    nominalEndTime="2024-06-12T18:00:29.935000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="c7d3c528-bab9-6376-729b-f5ac108ba3d0"),
                    job=Job(namespace="CheckFile", name="DataPublisher"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="DataPublisher"),
        eventType=RunState.COMPLETE,
        outputs=[
            OutputDataset(
                namespace="StoreSystem",
                name="DSCatalog",
                facets={"version": DatasetVersionDatasetFacet(datasetVersion="1.0")},
                outputFacets={},
            ),
            OutputDataset(
                namespace="StoreSystem",
                name="DSRows",
                facets={"version": DatasetVersionDatasetFacet(datasetVersion="1.0")},
                outputFacets={},
            ),
            OutputDataset(
                namespace="StoreSystem",
                name="PipelineMetadata",
                facets={"version": DatasetVersionDatasetFacet(datasetVersion="1.2")},
                outputFacets={},
            ),
        ],
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:31.860000+00:00",
        run=Run(
            runId="52783a0c-3b39-6f2c-1afa-b284723b2908",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="3df12357-a207-53f5-cf9f-731a7e332c33"),
                    job=Job(namespace="CheckFile", name="DataPublisher"),
                )
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineNotify"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:31.882000+00:00",
        run=Run(
            runId="dc71ad49-e62f-c68f-8392-eda159289f36",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:31.860000+00:00",
                    nominalEndTime="2024-06-12T18:00:31.882000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="52783a0c-3b39-6f2c-1afa-b284723b2908"),
                    job=Job(namespace="Pipeline", name="PipelineNotify"),
                ),
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineNotify"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:10.970000+00:00",
        run=Run(
            runId="863e4455-10ea-ad0b-6631-e940e22e803b",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:10.970000+00:00",
                    nominalEndTime="2024-06-12T18:00:10.970000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="f4a71764-2bf0-aa3e-18db-3d83a0e6c162"),
                    job=Job(namespace="CheckFile", name="Transform"),
                ),
            },
        ),
        job=Job(namespace="CheckFile", name="Transform"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:32.548000+00:00",
        run=Run(
            runId="62f85632-f08f-0d69-4de4-7b7a2b3677aa",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="863e4455-10ea-ad0b-6631-e940e22e803b"),
                    job=Job(namespace="CheckFile", name="Transform"),
                )
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineMerge"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:32.563000+00:00",
        run=Run(
            runId="a5c05035-efaf-e250-a449-3adb83b65a60",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:32.548000+00:00",
                    nominalEndTime="2024-06-12T18:00:32.563000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="62f85632-f08f-0d69-4de4-7b7a2b3677aa"),
                    job=Job(namespace="Pipeline", name="PipelineMerge"),
                ),
            },
        ),
        job=Job(namespace="Pipeline", name="PipelineMerge"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:29.967000+00:00",
        run=Run(
            runId="997a61ff-4db1-2f76-9626-3c592dbc651a",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:29.967000+00:00",
                    nominalEndTime="2024-06-12T18:00:29.967000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="90737031-3ca8-f6a6-adc3-a6b5297c9385"),
                    job=Job(namespace="Validation", name="validateData"),
                ),
            },
        ),
        job=Job(namespace="Validation", name="validateData"),
        eventType=RunState.COMPLETE,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:33.960000+00:00",
        run=Run(
            runId="64ee1c97-4fbd-90de-5afe-0100f53fe671",
            facets={
                "parent": ParentRunFacet(
                    run=Run(runId="997a61ff-4db1-2f76-9626-3c592dbc651a"),
                    job=Job(namespace="Validation", name="validateData"),
                )
            },
        ),
        job=Job(namespace="Pipeline", name="PipelinePause"),
        eventType=RunState.START,
    ),
    RunEvent(
        eventTime="2024-06-12T18:00:34.277000+00:00",
        run=Run(
            runId="67cadb22-765f-c90b-093b-a09fa3bc2098",
            facets={
                "nominalTime": NominalTimeRunFacet(
                    nominalStartTime="2024-06-12T18:00:33.960000+00:00",
                    nominalEndTime="2024-06-12T18:00:34.277000+00:00",
                ),
                "parent": ParentRunFacet(
                    run=Run(runId="64ee1c97-4fbd-90de-5afe-0100f53fe671"),
                    job=Job(namespace="Pipeline", name="PipelinePause"),
                ),
            },
        ),
        job=Job(namespace="Pipeline", name="PipelinePause"),
        eventType=RunState.COMPLETE,
    ),
]

client = OpenLineageClient(
    transport=HttpTransport(
        HttpConfig(
            url="http://127.0.0.1:8080",
            endpoint="openapi/openlineage/api/v1/lineage",
        )
    )
)

for event in events:
    client.emit(event)
