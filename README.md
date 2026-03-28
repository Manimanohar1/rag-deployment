# Air-Gapped AI Inference & RAG Pipeline (PoC)

A lightweight Proof-of-Concept (PoC) designed to evaluate the deployment and orchestration of localized Large Language Models (LLMs) and vector databases within a constrained, air-gapped Kubernetes environment.

This project demonstrates how to orchestrate local AI components without relying on external cloud APIs, simulating a highly secure, on-premise infrastructure deployment.

## 🏗️ Architecture Overview

The pipeline is contained entirely within the local cluster, utilizing local network routing and Python to bridge raw telemetry data with the inference engine.

* **Inference Engine:** A locally hosted LLM (e.g., Ollama/TinyLlama) running natively within the environment to handle data generation and embeddings without outbound internet access.
* **Stateful Vector Storage:** An in-memory Qdrant database utilized to store mathematical vector embeddings for context-aware queries.
* **Data Ingestion & Orchestration:** Custom Python automation and `curl` commands used to structure payloads, generate embeddings via the local model, and write them to the vector database.

## 🛠️ Tech Stack

* **Infrastructure:** Kubernetes (KodeKloud Sandbox Environment)
* **Local AI/Inference:** Ollama (or equivalent local model runner)
* **Database:** Qdrant (Vector DB)
* **Automation:** Python, Bash (`curl`), JSON

## ⚙️ Core Operations

This PoC successfully validated the following local integrations:

1. **Local Model Deployment:** Spinning up the inference engine within the cluster and exposing its internal API endpoints for local routing.
2. **Vector DB Initialization:** Deploying Qdrant as a local data store to handle high-dimensional vector arrays.
3. **Internal API Routing:** Using Python and `curl` to format text logs, post them to the local embedding model, and successfully insert the resulting vectors into Qdrant.
4. **Context Retrieval:** Querying the local vector database to retrieve specific logs and passing them back to the local LLM for localized analysis.

## 📈 Phase 2 Roadmap (Target Architecture)

Having validated the core component interactions in a sandbox environment, the next architectural iteration focuses on production-grade reliability:
* **Infrastructure-as-Code (IaC):** Migrating the deployment logic into Helm charts and managing state via GitOps (ArgoCD).
* **High-Performance Inference:** Transitioning from developer tools (Ollama) to enterprise-grade distributed inference engines (vLLM).
* **Traffic Management:** Implementing Istio to handle intelligent, token-aware routing across multiple inference pods.
