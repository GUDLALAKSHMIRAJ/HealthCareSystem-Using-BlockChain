// scripts/deploy_alt.js
import fs from "fs";
import path from "path";
import { ethers } from "ethers";

async function main() {
  // Load compiled artifact (adjust path if necessary)
  const artifactPath = path.join("artifacts", "contracts", "Report.sol", "Report.json");
  const artifact = JSON.parse(fs.readFileSync(artifactPath, "utf8"));

  // Connect to local Hardhat node (we started it on port 7545)
  const provider = new ethers.JsonRpcProvider("http://127.0.0.1:7545");

  // Use the first Hardhat account's private key (safe for local dev)
  const PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80";
  const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

  console.log("Using address:", await wallet.getAddress());

  // Create factory and deploy
  const factory = new ethers.ContractFactory(artifact.abi, artifact.bytecode, wallet);
  const contract = await factory.deploy(); // send deployment tx
  console.log("Transaction hash:", contract.deploymentTransaction().hash);

  // Wait for deployment to be mined
  await contract.waitForDeployment();

  // Print deployed address
  console.log("Contract deployed to:", await contract.getAddress());
}

main().catch((err) => {
  console.error("Deploy failed:", err);
  process.exitCode = 1;
});
