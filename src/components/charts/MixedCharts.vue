<script setup>
import { ref, defineProps, onMounted } from "vue";
import VueApexCharts from "vue3-apexcharts";

const props = defineProps(["chart_config", "activeChart", "series"]);

const chartOptions = ref({
	series: props.series,
	chart: {
		height: 350,
		type: "line",
	},
	stroke: {
		width: [0, 4],
	},
	dataLabels: {
		enabled: false,
		enabledOnSeries: [1],
	},
	labels: [
		"01 Jan 2001",
		"02 Jan 2001",
		"03 Jan 2001",
		"04 Jan 2001",
		"05 Jan 2001",
		"06 Jan 2001",
		"07 Jan 2001",
		"08 Jan 2001",
		"09 Jan 2001",
		"10 Jan 2001",
		"11 Jan 2001",
		"12 Jan 2001",
	],
	xaxis: {
		type: "datetime",
	},
	color: ["#ffffcc", "#ccffcc"],
	yaxis: [
		{
			title: {
				text: "Website Blog",
			},
			color: "#ffffcc",
		},
		{
			opposite: true,
			title: {
				text: "Social Media",
			},
			color: "#ccffcc",
		},
	],
});

const chartRef = ref(null);

onMounted(() => {
	// Access the chart instance using chartRef.value if needed
});
</script>

<template>
	<div v-if="activeChart === 'MixedCharts'">
		<vue-apex-charts
			:options="chartOptions"
			:series="
				props.series.map((s, index) => ({
					...s,
					type: index === 0 ? 'column' : 'line',
				}))
			"
			ref="chartRef"
		></vue-apex-charts>
	</div>
</template>
