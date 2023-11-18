<script setup>
import { ref, onMounted } from "vue";
import VueApexCharts from "vue-apexcharts";
const props = defineProps(["chart_config", "activeChart", "series"]);
console.log(props.series[0].data);
const chartOptions = ref({
	series: props.series[0].data,
	chart: {
		type: "polarArea",
	},
	stroke: {
		colors: ["#fff"],
	},
	fill: {
		opacity: 0.8,
	},
	responsive: [
		{
			breakpoint: 480,
			options: {
				chart: {
					width: 200,
				},
				legend: {
					position: "bottom",
				},
			},
		},
	],
});

const chart = ref(null);

onMounted(() => {
	const options = chartOptions.value;
	chart.value = new ApexCharts(document.querySelector("#chart"), options);
	chart.value.render();
});
</script>

<template>
	<div>
		<div id="chart" style="width: 100%"></div>
	</div>
</template>
