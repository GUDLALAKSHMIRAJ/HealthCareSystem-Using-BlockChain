import hre from "hardhat";

async function main() {
  const Report = await hre.ethers.getContractFactory("Report");
  const report = await Report.deploy();

  await report.waitForDeployment();

  console.log("Contract deployed to:", await report.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
