Mattermost feature labels
==========================

Mattermost’s feature labels serve as indicators of the status, maturity, and support level of each feature, helping users and system administrators navigate product feature adoption with clarity and confidence. Feature labels communicate the stage of development, level of readiness, and potential risks associated with a feature for customers seeking to adopt new value.

Experimental
-------------

Feature is an early Proof of Concept (POC) with an unstable codebase, minimal QA covering a small or specific set of use cases, and potential UI issues. Security reviews are incomplete, making it unsuitable for production. Distribution of the solution is limited, and our Cloud environments are typically not eligible to use experimental features. Data loss can occur as data schemas and configurations may change, and minimal documentation is available. Caution is advised as the solution may be discarded if its value is not proven.

Beta
-----

Feature is in active development towards General Availability. Not fully complete, but reviewed by our security team, adoption is suitable for a small set of customers behind a feature flag. Identified bugs are fixed on a best effort basis, and no major breaking changes are anticipated, full testing is in progress, and detailed documentation may not be available. Beta is a transitional stage, meaning the solution is maturing but requires careful consideration in a full production deployment as scale and client availability may vary. `Premier Support <https://mattermost.com/support/>`__ is recommended when using beta features in production environments. 

General Availability
---------------------

Feature has undergone thorough validation and testing and has production-level quality. It is feature-complete, meets quality standards, has successfully passed security reviews, and has detailed product documentation available. General Availability features are suitable for widespread production deployment and adoption, and are eligible for commercial support, as they offer stability and reliability, with no expected changes that could disrupt functionality or scalability.

Deprecated
-----------

Feature is officially marked for removal from the product. It is no longer supported or actively maintained by the development team. If the feature is still in use in your deployed version, we recommend users discontinue its use and migrate to alternative functionalities.




